# GOPH 420 - Inversion and Parameter Estimation for 
Geophysicists
*Semester:* W2023 
*Instructor:* B. Karchewski 
*Author:* <Carla Acosta>
*Topic:* Least Squares Regression

This code Perform multiple linear regression.

Parameters
----------
y : array_like, shape = (n,) or (n,1) #The vector of dependent variable data
Z : array_like, shape = (n,m) # The matrix of independent variable data

Returns
-------
numpy.ndarray, shape = (m,) or (m,1) #The vector of model coefficients
numpy.ndarray, shape = (n,) or (n,1) # The vector of residuals
float # The coefficient of determination, r^2