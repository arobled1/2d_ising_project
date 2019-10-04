#=============================================================================80
# Description:
# Finds the dominant eigenvalue and associated eigenvector of the transfer
# matrix, as described in paper by Lim and Weare, using the Power Method,
# aka Power Iteration.
# The user must specify an intial vector to represent the dominant eigenvector.
# The initial vector is usually chosen to be an array of ones or some unit
# vector (e.g. [1 0 0]).
# Python 3.7.4 was used.
#===============================================================================
# Author: Alan Robledo
# Modified Date: 10/4/19
#===============================================================================
# Output:
# Iteration #: 505
# Dominant eigenvalue is: 2.613278478020
#===============================================================================
# Note:
#   Decreasing the value of the tolerance will mean more iterations needed for
#   convergence.
#===============================================================================
import time
import numpy as np
import generate_full
import numba
from numba import jit

@jit(nopython=True)
def power_iter(max_iterations, tolerance, matrix, vec):
    # Finding l-infinity norm of initial vector x
    xp = max(max(vec),-min(vec))
    # Rescaling the initial vector to prevent from blowing up
    vec = vec / xp
    i = 0
    while i < max_iterations:
        i += 1
        # Reset y before matrix multiply
        y = np.zeros(d)
        # Matrix multiplying A with the initial vector x
        for j in range(d):
            even = j//2
            shift1 = j//2 + 2**(n-1)
            odd = (j-1)//2
            shift2 = (j-1)//2 + 2**(n-1)
            if j % 2 == 0:
                y[j] = matrix[j][even] * vec[even] + matrix[j][shift1] * vec[shift1]
            else:
                y[j] = matrix[j][odd] * vec[odd] + matrix[j][shift2] * vec[shift2]
        # Finding the l-infinity norm of the result from Ax.
        # This serves as the dominant eigenvalue.
        eig_val = max(max(y),-min(y))
        error = max(max(vec - (y/eig_val)),-min(vec - (y/eig_val)))
        vec = y / eig_val
        # If you want to see eigenvalue at each iteration, uncomment line below
    #    print("Iteration #:",i,"    Eigenvalue:",eig_val)
        if error < tolerance:
            break
    return i, eig_val

n = 5     # number of spins
d = 2**n  # matrix dimension dxd
b = 0.01  # magnetic field strength
t = 2.2   # temperature

# Setting initial guess vector
init_vec = np.zeros(d)
init_vec[0] = 1
# Max number of iterations (set by user)
max_iter = 600
# Tolerance (set by user)
tol = 10**-7

# Bottom block gives complilation time + runtime
start = time.time()
trans_mat = generate_full.tran_mat(n, b, t)
power_iter(max_iter, tol, trans_mat, init_vec)
end = time.time()

# Bottom block is just for runtime
start = time.time()
trans_mat = generate_full.tran_mat(n, b, t)
iterations, eigenvalue = power_iter(max_iter, tol, trans_mat, init_vec)
end = time.time()

eig_file = open("data.dat", 'w')
if iterations == max_iter:
    eig_file.write("Exceeded max iterations. Try a new initial vector.\n")
    eig_file.write("Number of iterations: %d\n" % iterations)
else:
    eig_file.write("Success!\n")
    eig_file.write("Number of iterations: %d\n" % iterations)
eig_file.write("Dominant eigenvalue is: %.12f\n" % eigenvalue)
eig_file.write("Time (in seconds): %.12f" % (end - start))
eig_file.close()
print("Check 'data.dat' for results!")
