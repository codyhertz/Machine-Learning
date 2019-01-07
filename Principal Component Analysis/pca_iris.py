from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from itertools import cycle

iris = load_iris()

numSamples, numFeatures = iris.data.shape
print(numSamples, numFeatures, list(iris.target_names))

x = iris.data
pca = PCA(n_components=2, whiten=True).fit(x)

x_pca = pca.transform(x)
print(pca.components_)

print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))

colors = cycle('rgb')
target_ids = range(len(iris.target_names))
plt.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):
    plt.scatter(x_pca[iris.target == i, 0], x_pca[iris.target == i, 1], c=c, label=label)

plt.legend()
plt.show()
