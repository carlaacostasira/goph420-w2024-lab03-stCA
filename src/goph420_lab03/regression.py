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
#
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
    y = np.array(y)
    Z = np.array(Z)
    
    # Create a column of ones with the same number of rows as Z
    ones_column = np.ones((Z.shape[0], 1))
    
    # Concatenate the column of ones with Z to form the new Z matrix
    Z = np.concatenate((ones_column, Z[:, np.newaxis]), axis=1) 
    
    Z_transpose = np.transpose(Z) # Transpose the matrix Z
    ZTZ = np.dot(Z_transpose, Z) # Compute the product of Z_transpose and Z
    ZTZ_inv = np.linalg.inv(ZTZ) # Compute the inverse of ZTZ
    ZTY = np.dot(Z_transpose, y) # Compute
    coeffs = np.dot(ZTZ_inv, ZTY) # Compute the coefficients
    # coeffs = np.linalg.lstsq(Z, y)[0] # Perform the regression
    residuals = y - np.dot(Z, coeffs) # Compute the residuals
    ybar = np.mean(y) # Compute the mean of y
    sstot = np.sum((y - ybar) ** 2) # Compute the total sum of squares
    ssres = np.sum(residuals ** 2) # Compute the sum of squared residuals
    r2 = 1 - ssres / sstot # Compute the r2

    return coeffs, residuals, r2
