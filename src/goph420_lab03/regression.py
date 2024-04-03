import numpy as np
import matplotlib.pyplot as plt

def multi_regress(y, Z):
# """Perform multiple linear regression.
# Parameters
# ----------
# y : array_like, shape = (n,) or (n,1)
# The vector of dependent variable data
# Z : array_like, shape = (n,m)
# The matrix of independent variable data
# Returns
# -------
# numpy.ndarray, shape = (m,) or (m,1)
# The vector of model coefficients
# numpy.ndarray, shape = (n,) or (n,1)
# The vector of residuals
# float
# The coefficient of determination, r^2
# """

# Convert the input data to numpy arrays
    n,m = Z.shape
    y = np.array([])
    Z = np.array([])
    Z = np.column_stack((np.ones(n), Z[:, 1]))
        

    coeffs = np.linalg.lstsq(Z, y)[0] # Perform the regression
    residuals = y - np.dot(Z, coeffs) # Compute the residuals
    ybar = np.mean(y) # Compute the mean of y
    sstot = np.sum((y - ybar) ** 2) # Compute the total sum of squares
    ssres = np.sum(residuals ** 2) # Compute the sum of squared residuals
    r2 = 1 - ssres / sstot # Compute the r2

    return coeffs, residuals, r2
