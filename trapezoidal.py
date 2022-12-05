import numpy as np


def polynomial():
    """_summary_
        converts the comma-separated values to polynomial function and prints it out
        It also stores it in a variable POLY to be used for other computations
        This function has no return value
    """
    global POLY, DELTA_X, F_1,F_n
    POLY = np.poly1d(MY_FUNCTION)

    print(POLY)
    F_1 = POLY(LOWER)
    F_n = POLY(UPPER)
    DELTA_X = (UPPER-LOWER)/INTERVALS

def convert():
    """_summary_
       Obtains the outputs (y) of the functions for each input(x) 

    Returns:
        _list_: _list of the codomain_
    """
    global POINTS, OUTPUTS
    POINTS = []
    lower_limit = LOWER
    while True:
        new=lower_limit+DELTA_X
        if new < UPPER:
            POINTS.append(new)
            lower_limit=new
        else:
            break

    OUTPUTS = [POLY(point) for point in POINTS]
    return OUTPUTS

def finish():
    """_summary_
        Calculates the approximate value of the area under the given curve and stores it in a variable
    Returns:
        _float_: _The approximate value of the area under the curve to 3 places of decimal where applicable_
    """

    for number in OUTPUTS:
        OUTPUTS[OUTPUTS.index(number)] = 2*number

    total = sum(OUTPUTS)+F_1+F_n

    Area = (DELTA_X*0.5)*total
    return Area

def trapezoidal(a,b,n,*args):
    """_summary_

    Args:
        a (float): _upper limit of the function_
        b (float): _lower limit of the function_
        n (int): _number of intervals_
        args (comma-separated integers): _comma-separated integer coefficients of decreasing values of variable in function. Represent value as 0 where power of x does not exist in the function_
    """
    global UPPER,LOWER,INTERVALS,MY_FUNCTION,MY_FUNCT
    UPPER = a
    LOWER = b
    INTERVALS = n
    MY_FUNCT = list(args)
    MY_FUNCTION = [int(i) for i in MY_FUNCT]
    
    polynomial()
    convert()
    print(round(finish(),3))