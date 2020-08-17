## The Lagrange polynomial
Given a set of coordinates {(*x*<sub>1</sub>, *y*<sub>1</sub>), (*x*<sub>2</sub>, *y*<sub>2</sub>), **...** , (*x<sub>n</sub>*, *y<sub>n</sub>*)}, we can construct a polynomial *L*(*x*), with at most degree *n*, which passes through all these coordinates. The Lagrange polynomial is the lowest degree polynomial that we can construct.

When constructing the Lagrange polynomial of a function *f*, we take an interval [*x*<sub>1</sub>, *x*<sub>*n*</sub>], and choose a set of points {*x*<sub>1</sub>, *x*<sub>2</sub>, **...** , *x<sub>n</sub>*}. We then take the set of coordinates to be {(*x*<sub>1</sub>, *f*(*x*<sub>1</sub>)), (*x*<sub>2</sub>, *f*(*x*<sub>2</sub>)), **...** , (*x<sub>n</sub>*, *f*(*x<sub>n</sub>*))}.

## Runge's phenomenon
If you use equispaced points in your interval, the Lagrange polynomial sees large oscillations near the boundaries as you increase its degree (by adding more points in the interval). This is known as Runge's phenomenon.

## Chebyshev nodes
Chebyshev nodes (in an interval) are essentially a set of numbers that cluster at the boundary of the interval, and spread out towards the centre. These are useful for constructing Lagrange polynomials because they minimise the effect of Runge's phenomenon, as we will see in the investigation.

# Investigation
We'll look at two functions
- *f*(*x*) = |*x*|
- *g*(*x*) = 1/(1+10*x*<sup>2</sup>)

and construct 50 Lagrange polynomials of degree 0-49 for each function, in the interval [-1, 1].

We'll do this twice, first with a set of equispaced points, and then with a set of Chebyshev nodes to see if we do indeed minimise the effect of Runge's phenomenon.

To obtain the maximum error, we'll calculate the difference between a function and its respective Lagrange polynomial over 500 equispaced points, in the interval [-1, 1], and take the maximum value.
