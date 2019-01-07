from sklearn.linear_model import LogisticRegression
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

print(x_train[0:5])
print(y_train[0:5])
log_reg = LogisticRegression(C=100)
log_reg.fit(x_train, y_train)

acc_train = log_reg.score(x_train, y_train)
acc_test = log_reg.score(x_test, y_test)
print('Accuracy:', (acc_train + acc_test) / 2)

accuracy = (acc_train + acc_test) / 2

print(log_reg.predict([x_train[0]]))

dump(log_reg, 'log_reg_model.joblib')

dandy = load('log_reg_model.joblib')

print(dandy.predict([x_train[0]]))
