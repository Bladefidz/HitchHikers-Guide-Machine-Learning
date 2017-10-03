import matplotlib.pyplot as plt
import numpy as np
from sample_data import *
from LReg import LReg

# Compute Linear Regression of x and y
ls = LReg(x, y)
print("r = ",ls.correlation)
print("b = ",ls.slope)
print("a = ",ls.intercept)

# Regression line or fit function
f = lambda x: ls.slope * x + ls.intercept

# Plot regression line
plt.scatter(x, y)
x = np.array([min(x), max(x)])
plt.plot(x, f(x), label='Regression line')
plt.legend()
plt.show()