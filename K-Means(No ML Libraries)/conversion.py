import copy

def convertToAPointValuesKMeans(cluster):
    cluster2 = copy.deepcopy(cluster)

    for i in range(len(cluster2)):
        if cluster2[i] == [2, 10]:
            cluster2[i] = 'A1'
        if cluster2[i] == [2, 5]:
            cluster2[i] = 'A2'
        if cluster2[i] == [8, 4]:
            cluster2[i] = 'A3'
        if cluster2[i] == [5, 8]:
            cluster2[i] = 'A4'
        if cluster2[i] == [7, 5]:
            cluster2[i] = 'A5'
        if cluster2[i] == [6, 4]:
            cluster2[i] = 'A6'
        if cluster2[i] == [1, 2]:
            cluster2[i] = 'A7'
        if cluster2[i] == [4, 9]:
            cluster2[i] = 'A8'

    return cluster2

def convertToAPointValuesHierarchical(cluster):
    cluster2 = copy.deepcopy(cluster)

    for i in range(len(cluster2)):
        if cluster2[i] == [2, 2]:
            cluster2[i] = 'A1'
        if cluster2[i] == [3.01, 2]:
            cluster2[i] = 'A2'
        if cluster2[i] == [4.02, 2]:
            cluster2[i] = 'A3'
        if cluster2[i] == [5.03, 2]:
            cluster2[i] = 'A4'
        if cluster2[i] == [6.04, 2]:
            cluster2[i] = 'A5'
        if cluster2[i] == [7.05, 2]:
            cluster2[i] = 'A6'
        if cluster2[i] == [2, 3.5]:
            cluster2[i] = 'A7'
        if cluster2[i] == [3.01, 3.5]:
            cluster2[i] = 'A8'
        if cluster2[i] == [4.02, 3.5]:
            cluster2[i] = 'A9'
        if cluster2[i] == [5.03, 3.5]:
            cluster2[i] = 'A10'
        if cluster2[i] == [6.04, 3.5]:
            cluster2[i] = 'A11'
        if cluster2[i] == [7.05, 3.5]:
            cluster2[i] = 'A12'

    return cluster2
