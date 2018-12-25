from hierarchical_alg import hierarchicalClustering

s = [[[2, 2]],
     [[3.01, 2]],
     [[4.02, 2]],
     [[5.03, 2]],
     [[6.04, 2]],
     [[7.05, 2]],
     [[2, 3.5]],
     [[3.01, 3.5]],
     [[4.02, 3.5]],
     [[5.03, 3.5]],
     [[6.04, 3.5]],
     [[7.05, 3.5]]]

print('#######################################################################')
print()
print('Hierarchical Clustering with Single Linkage for k = 2')
print()
hierarchicalClustering(s, 2, 'single')
print()
print('#######################################################################')
print()
print('Hierarchical Clustering with Single Linkage for k = 6')
print()
hierarchicalClustering(s, 6, 'single')
print()
print('#######################################################################')
print()
print('Hierarchical Clustering with Complete Linkage for k = 2')
hierarchicalClustering(s, 2, 'complete')
print()
print('#######################################################################')
print()
print('Hierarchical Clustering with Complete Linkage for k = 6')
hierarchicalClustering(s, 6, 'complete')
print()
print('#######################################################################')
