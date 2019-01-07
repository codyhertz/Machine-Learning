from sklearn import svm, datasets
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
import numpy as np
import random

# k clusters of n people income/age
def createClusterdData(N, k):
    pointsPerCluster = float(N) / k

    x = []
    y = []
    for i in range(k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)

        for j in range(int(pointsPerCluster)):
            x.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
            y.append(i)

    x = np.array(x)
    y = np.array(y)
    return x, y

(x, y) = createClusterdData(1000, 5)

c = 1.0
svc = svm.SVC(kernel='linear', C=c).fit(x, y)

def plotPredictions(clf):
    print('Ploting...')
    xx, yy = np.meshgrid(np.arange(0, 250000, 10), np.arange(10, 70, 0.5))
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    plt.figure(figsize=(8, 6))
    z = z.reshape(xx.shape)
    plt.contourf(xx, yy, z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(x[:,0], x[:,1], c=y.astype(np.float))
    plt.show()

plotPredictions(svc)

print(svm.predict([200000, 40]))
