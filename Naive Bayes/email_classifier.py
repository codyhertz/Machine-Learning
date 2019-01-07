import os
import io
import numpy as np
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            # inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                line = re.sub(r"\s+", '', line)
                if line is not '':
                    lines.append(line)

            f.close()
            message = '\n'.join(lines)
            yield path, message

def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class': []})
data = data.append(dataFrameFromDirectory('./emails/spam', 'spam'))
data = data.append(dataFrameFromDirectory('./emails/ham', 'ham'))

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

examples = ['Free Viagra now!!!', "Hi Bob, how abou a game of golf tomorrow?"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print(predictions)
