from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# create a sample data set
X = np.array([[1, 2],
              [3, 4]])

# create polynomial features up to degree 2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# display the updated feature matrix
print(X_poly)