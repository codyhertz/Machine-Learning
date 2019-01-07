import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

poly_model = np.poly1d(np.polyfit(x, y, 4))

xp = np.linspace(0, 7, 100)
print('R^2 Value:', r2_score(y, poly_model(x)))
plt.scatter(x, y)
plt.plot(xp, poly_model(xp), c='r')
plt.show()
