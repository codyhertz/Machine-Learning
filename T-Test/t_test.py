import numpy as np
from scipy import stats

a = np.random.normal(25.0, 5.0, 10000)
b = np.random.normal(26.0, 5.0, 10000)

print(stats.ttest_ind(a, b)) # bad change, with a ery low chance of randomness

b = np.random.normal(25.0, 5.0, 10000)
print(stats.ttest_ind(a, b)) # no change, outcome is likely random
