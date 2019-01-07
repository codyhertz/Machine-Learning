import numpy as np
import matplotlib.pyplot as plt


incomes = np.random.normal(27000, 15000, 10000)
incomes = np.append(incomes, [1000000000])

def reject_outliers(data):
    u = np.median(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered

filtered = reject_outliers(incomes)

plt.hist(filtered, 50)
plt.show(]\)
