from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
from joblib import dump, load


def create_feature_sets_and_labels_complex_nn():
    game_data = np.genfromtxt('game_data_normalized_small.csv', delimiter=',', dtype="float32")

    testing_size = int(.5 * len(game_data))

    train_y = list(game_data[:, 2][:-testing_size])

    test_y = list(game_data[:, 2][:-testing_size])


    train_x = []
    for i in game_data[:-testing_size]:
        train_x.append(list(i[np.arange(len(i))!=2]))

    test_x = []
    for i in game_data[-testing_size:]:
        test_x.append(list(i[np.arange(len(i))!=2]))

    train_x = np.array(train_x)
    test_x = np.array(test_x)

    train_y = np.array(train_y)
    test_y = np.array(test_y)

    return train_x, train_y, test_x, test_y


x_train, y_train, x_test, y_test = create_feature_sets_and_labels_complex_nn()


svmModel = svm.SVC(kernel='poly', gamma='scale', cache_size=7000)
svmModel.fit(x_train, y_train)
acc_train = svmModel.score(x_train, y_train)
acc_test = svmModel.score(x_test, y_test)
print('Accuracy:', (acc_train + acc_test) / 2)

accuracy = (acc_train + acc_test) / 2

print(svmModel.predict([x_train[0]]))

dump(svmModel, 'svm_model.joblib')

dandy = load('svm_model.joblib')

print(dandy.predict([x_train[0]]))
