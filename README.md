# Trapezoidal_Algorithm
Calculates the approximate area under a curve using the trapezoidal algorithm.

This program requires that the user calls the trapezoidal function with the upper limit, lower limit, number of intervals, and the function
or curve as arguments. 
While the upper and lower limits may be float, the number of intervals must be an integer.
The function is also written as comma-separated integers of the coefficients of decreasing powers of x.

Examples of a use case are demonstrated below:


Example 1:
For the function 2x^2 + 4x + 3, for the limits 0,10 and number of intervals of 10.
trapezoidal(10,0,10,2,4,3)

output: 900


Example 2:
For the function x^3 for the limits -1,3 and number of intervals of 15.
trapezoidal(3,-1,15,1,0,0,0)

output: 27.342

NB: Where applicable, the answer is given to 3 places of decimal