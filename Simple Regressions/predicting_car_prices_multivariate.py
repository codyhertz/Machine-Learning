import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler


scale = StandardScaler()

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

print(df.head())

x = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

x[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(x[['Mileage', 'Cylinder', 'Doors']].as_matrix())

print(x)

est = sm.OLS(y, x).fit()

print(est.summary())
