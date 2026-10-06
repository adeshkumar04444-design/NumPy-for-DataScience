# Why NumPy array is better than python list. and what's the need.

# Problem: Suppose a scientist wanted to find out the average temperature of millions of cities around the world.

# NumPy arrays were invented to solve problems of this kind. NumPy arrays are designed to handle large amounts of data and calculations.

import numpy as np

tempreatures = np.array([32.5, 31.8, 33.0, 35.2, 36.6])
average = np.mean(tempreatures)
print(average)


# NumPy developed by 'Travis Oliphant' in 2005.
# NumPy (Numerical Python) is a Python library used for fast numerical calculations and working with arrays and mathematical data.