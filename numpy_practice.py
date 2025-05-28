# numpy_practice.py
import numpy as np


# ****************************************
# 1) WORK WITH ARRAYS 
# ****************************************
# create new array with 10 linearly spaced numbers in [0, 9]
new_array_linspace = np.array(np.linspace(0, 9, 10))
# create new array with 10 integers in [0, 10)
new_array_arange = np.array(np.arange(0,10))
check = lambda x, y:  "Yes" if np.all(x == y) else "No"
print(f"Is `new_array_linspace` == `new_array_arange`?\t {check(new_array_linspace, new_array_arange)}")
# reshape `new_array` to have size 2x5
np.reshape(new_array_linspace, (2,5))
"""
Note: 
- for small arrays, Python's list comprehension often outperforms NumPy's boolean indexing (`mask`)
    because it incurs lower setup time and operates purely in C-optimized loop code.
- Yet, for large arrays and numerical workloads, NumPy's vectorized boolean indexing is better, as
    it leverages contiguous memory (lower memory use), avoids Python-level loops, and runs the
    filter entirely in optimized C under the hood
"""
# create boolean mask for Numpy array
mask = new_array_linspace % 2 == 0
new_array_linspace = new_array_linspace[mask]





# ****************************************
# 2) PIECEWISE LINEAR INTERPOLATOR
# ****************************************
import matplotlib.pyplot as plt
# data 
x = np.linspace(0, 10, num=11)
y = np.cos(-x**2 / 9.0)
# new data, that we want to use to interpolate `ynew`
xnew = np.linspace(0, 10, num=1001)
ynew = np.interp(xnew, x, y)
# plot
plt.plot(xnew, ynew, '-', label='linear interp')
plt.plot(x, y, 'o', label='data')
plt.legend(loc='best')
plt.show()