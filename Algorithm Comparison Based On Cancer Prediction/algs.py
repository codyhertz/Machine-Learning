import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn import tree
import pydot
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import svm, neighbors
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier


masses_data = pd.read_csv('mammographic_masses.data.txt', na_values=['?'], names=['BI-RADs', 'age', 'shape', 'margin', 'density', 'severity'])
masses_data.dropna(inplace=True)

all_features = masses_data[['age', 'shape', 'margin', 'density']].values
all_classes = masses_data['severity'].values

feature_names = ['age', 'shape', 'margin', 'density']

scaler = preprocessing.StandardScaler()
all_features_scaled = scaler.fit_transform(all_features)

np.random.seed(1234)
(training_inputs, testing_inputs, training_classes, testing_classes) = train_test_split(all_features_scaled, all_classes, train_size=0.75, random_state=1)

d_tree = DecisionTreeClassifier(random_state=1)
d_tree.fit(training_inputs, training_classes)

dot_data = StringIO()
tree.export_graphviz(d_tree, out_file=dot_data, feature_names=feature_names)
(graph,) = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("decision_tree.pdf")

print('This program uses Mammographic Masses data to compare different machine learning algorithms.\n')
print("Decision Tree Accuracy:", d_tree.score(testing_inputs, testing_classes))

random_forest = RandomForestClassifier(n_estimators=10, random_state=1)
print('Random Forest Accuracy:', cross_val_score(random_forest, all_features_scaled, all_classes, cv=10).mean())

svc = svm.SVC(kernel='linear', gamma='scale', C=1.0)
print('Linear SVM Accuracy:', cross_val_score(svc, all_features_scaled, all_classes, cv=10).mean())

svc = svm.SVC(kernel='rbf', gamma='scale', C=1.0)
print('RBF SVM Accuracy:', cross_val_score(svc, all_features_scaled, all_classes, cv=10).mean())

svc = svm.SVC(kernel='sigmoid', gamma='scale', C=1.0)
print('Sigmoid SVM Accuracy:', cross_val_score(svc, all_features_scaled, all_classes, cv=10).mean())

svc = svm.SVC(kernel='poly', gamma='scale', C=1.0)
print('Polynomial SVM Accuracy:', cross_val_score(svc, all_features_scaled, all_classes, cv=10).mean())

k_nn = neighbors.KNeighborsClassifier(n_neighbors=14)
print('K Nearest Neighbors, where K=14, Accuracy:', cross_val_score(k_nn, all_features_scaled, all_classes, cv=10).mean())

scaler = preprocessing.MinMaxScaler()
all_features_minmax = scaler.fit_transform(all_features)

naive_bayes = MultinomialNB()
print('Multinomial Naive Bayes Accuracy:', cross_val_score(naive_bayes, all_features_minmax, all_classes, cv=10).mean())

log_reg = LogisticRegression()
print('Logistic Regression Accuracy:', cross_val_score(log_reg, all_features_scaled, all_classes, cv=10).mean())

def create_model():
    model = Sequential()
    model.add(Dense(15, input_dim=4, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(13, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(11, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

estimator = KerasClassifier(build_fn=create_model, epochs=75, verbose=0)
print('5 Layer Deep Neural Network Accuracy:', cross_val_score(estimator, all_features_scaled, all_classes, cv=10).mean())
