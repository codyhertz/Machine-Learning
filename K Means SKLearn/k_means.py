from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
import numpy as np
import random

# k clusters of n people income/age
def createClusterdData(N, k):
    pointsPerCluster = float(N) / k

    x = []
    for i in range(k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)

        for j in range(int(pointsPerCluster)):
            x.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])

    x = np.array(x)
    return x

data = createClusterdData(10000, 5)

model = KMeans(n_clusters=5)
model = model.fit(scale(data)) # normalizing
print(model.labels_) # print cluster each person was put at

plt.figure(figsize=(8, 6))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(np.float))
plt.show()
