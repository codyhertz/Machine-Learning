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
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=features)

(graph,) = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("hired.pdf")
