def bisection_zero(f_x, a_0, b_0):
    """Uses bi-section method to find a single zero for a polynomial.
    Paramaters include: f_x: a polynomial function, a_0: Test point where
    f(a_0) < 0, b_0: Test point where f(b_0) > 0"""

    # Incase parameters are inputted incorrectly or polynomial does not
    # have zero (if the function doesn't cross the x axis, all values
    # are either positive of negative), return None.
    if calculate(f_x, a_0) > 0 or calculate(f_x, b_0) < 0:
        return None

    midpoint = (a_0 + b_0)/2
    lower = a_0
    upper = b_0
    loopcount = 0
    
    # Keep going until the f(midpoint) equals 0. When a zero is found.
    while (calculate(f_x, midpoint)) != 0:
        midpoint = (lower + upper)/2
        # Depending on if f(midpoint) is negative or positive, change
        # upper or lower bound accordingly.
        if (calculate(f_x, midpoint)) < 0:
            lower = midpoint
        else:
            upper = midpoint
        # In case the zero is a non terminating decimal,
        # program will stop running after 10 iterations.
        loopcount += 1
        if loopcount == 10:
            break
    # Return the x value of the zero rounded to 2 decimal places.
    return round(midpoint,2)
    

def calculate(f_x, x):
    """Computes the y value for a function for a given x value."""
    
    n = len(f_x)-1 # Degree of polynomial.
    sum = f_x[0]*(x**(n))
    for i in range(1,len(f_x)):
        # Multiplies each coefficient with appropriate exponent.
        # Then adds it all up.
        sum += f_x[i]*(x**(n-i)) 
    return sum

print(bisection_zero([1,-7,10],4,1))
