
def NewtonRaphson(fpoly, a, tol =.00001):
    """Given a set of polynomial coefficients fpoly
        for a univariate polynomial function, this function
        finds the real roots of the polynomial (if any)
        using the Newton-Raphson method.
        a is the initial estimate of the root and
        starting state of the search
        This is an iterative method that stops when the
        change in estimators is less than tolerance.
        """

    x = 1.0
    dif = 1.0
    while (dif > tol):
        b = polyval(fpoly, a)
        m = polyval(derivative(fpoly),a)
        x = -1*(b/m)
        dif = abs(x)
        a = a+x
    return a

def polyval(fpoly, x):
    """polyval(fpoly, x)
     Given a set of polynomial coefficients from highest order to x^0,
     compute the value of the polynomial at x. We assume zero
     coefficients are present in the coefficient list."""

    b = 0
    count = 0
    l = len(fpoly)
    while(count < l):
        b += fpoly[count] * (x ** (l - count-1))
        count += 1
    return b

def derivative(fpoly):
    """derivative(fpoly)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the derivative polynomial.
    returns a list"""

    l = len(fpoly)
    count = 0
    hpoly = []
    while(count < l-1):
        x = fpoly[count] * (l - count-1)
        hpoly.append(x)
        count += 1
    return hpoly
