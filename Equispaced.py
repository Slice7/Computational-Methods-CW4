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
f_error = np.zeros(n, dtype='float64')
g_error = np.zeros(n, dtype='float64')

for i in range(n):
    nvals = np.linspace(-1, 1, i+1)  # the interval used to construct the lagrange polynomial
    
    # Creating the lagrange polynomials
    L_f = scipy.interpolate.barycentric_interpolate(nvals, f(nvals), mvals)
    L_g = scipy.interpolate.barycentric_interpolate(nvals, g(nvals), mvals)
    
    # Calculating the error
    f_error[i] = np.max(np.abs(f(mvals) - L_f))
    g_error[i] = np.max(np.abs(g(mvals) - L_g))

plt.semilogy(f_error, label='f(x) error')
plt.semilogy(g_error, label='g(x) error')
plt.title('Equispaced interpolation points')
plt.xlabel('Degree of polynomial')
plt.ylabel('Max error')
plt.legend(loc='upper left')
plt.show()
"""We can see that as the degree increases, the error increases exponentially.
This is Runge's phenomenon in action."""
