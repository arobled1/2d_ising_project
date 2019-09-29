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
# Date: 9/26/19
#===============================================================================
# Output:
# Iteration #: 161
# Dominant eigenvalue is: 2.6145152555104674
#===============================================================================
# Note:
#   Decreasing the value of the tolerance will mean more iterations needed for
#   convergence.
#===============================================================================
import numpy as np
import generate

def power_iter(max_iterations, tolerance, values, columns, rows, vec):
    # Finding l-infinity norm of initial vector x
    xp = abs(max(vec, key=abs))
    # Rescaling the initial vector to prevent from blowing up
    vec = vec / xp
    i = 0
    while i < max_iterations:
        i += 1
        y = np.zeros(d)
        print("rows:",rows)
        print("values:", values)
        print("columns:", columns)
        # Matrix multiplying A with the initial vector x.
        # This is done using the CSR method.
        for j in range(d):
            k = rows[j]
            # If statement is added because code will not loop over the last row
            # of the transfer matrix. Edit later.
            if k == rows[d-1]:
                y[j] += values[k] * vec[columns[k]] + values[k+1] * vec[columns[k+1]]
                break
            while k < rows[j+1]:
                y[j] += values[k] * vec[columns[k]]
                k += 1
        # Finding the l-infinity norm of the result from Ax.
        # This serves as the dominant eigenvalue.
        eig_val = abs(max(y, key=abs))
        error = abs(max(vec - (y/eig_val), key=abs))
        vec = y / eig_val
        print("Iteration #:", i)
        print("Eigenvalue", eig_val)
        print("")
        if error < tolerance:
            print("Success!")
            print("Dominant eigenvalue is:", eig_val)
            print("Dominant eigenvector is:", vec)
            i = max_iterations + 1
        if i == max_iterations:
            print("Exceeded max iterations. Try a new initial vector.")
            print("Dominant eigenvalue is:", eig_val)
            print("Dominant eigenvector is:", vec)
        print("vec:", vec)
    return eig_val, vec

n = 3     # number of spins
d = 2**n  # matrix dimension dxd
b = 0.01  # magnetic field strength
t = 2.2   # temperature

# Setting initial guess vector
init_vec = np.zeros(d)
init_vec[0] = 1
# Max number of iterations (set by user)
max_iter = 200
# Tolerance (set by user)
tol = 10**-6

val, col, row_ptr = generate.tran_mat(n, b, t)
power_iter(max_iter, tol, val, col, row_ptr, init_vec)