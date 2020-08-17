import numpy as np
import scipy.interpolate
from matplotlib import pyplot as plt

def f(x):
    return np.abs(x)

def g(x):
    return 1./(1 + 10*np.power(x, 2))

n = 50  # Number of interpolation points
m = 500  # Number of points to evaluate the polynomial

mvals = np.linspace(-1, 1, m)  # the interval used to calculate error

# Reserve space for error data
fc_error = np.zeros(n, dtype='float64')
gc_error = np.zeros(n, dtype='float64')

for i in range(1, n+1):
    cvals = []
    for j in range(1, i+1):
        cvals.append(np.cos((2*j - 1)*np.pi/(2*i)))  # Creating Chebyshev points
        
    # Creating the lagrange polynomials
    L_fc = scipy.interpolate.barycentric_interpolate(cvals, f(cvals), mvals)
    L_gc = scipy.interpolate.barycentric_interpolate(cvals, g(cvals), mvals)
    
    # Calculating the error
    fc_error[i-1] = np.max(np.abs(f(mvals) - L_fc))
    gc_error[i-1] = np.max(np.abs(g(mvals) - L_gc))

plt.semilogy(fc_error, label='f(x) error')
plt.semilogy(gc_error, label='g(x) error')
plt.title('Chebyshev interpolation points')
plt.xlabel('Degree of polynomial')
plt.ylabel('Max error')
plt.legend()
plt.show()
"""Using Chebyshev nodes, we can see that we've mitigated the effects of Runge's phenomenon.
The error indeed decreases exponentially."""
