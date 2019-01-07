from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn import tree
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydot

input_file = "./PastHires.csv"
df = pd.read_csv(input_file, header=0)

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)

features = list(df.columns[:6])

y = df['Hired']
x = df[features]

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(x, y)

print(clf.predict([[10, 1, 4, 0, 0, 0]]))
print(clf.predict([[10, 0, 4, 0, 0, 0]]))
