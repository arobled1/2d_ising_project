import numpy as np

def power_iter(max_iterations, tolerance, matrix, vec):
    # Finding l-infinity norm of initial vector x
    xp = abs(max(vec, key=abs))
    # Rescaling the initial vector to prevent from blowing up
    vec = vec / xp
    i = 0
    while i < max_iterations:
        i += 1
        # Matrix multiplying A with the initial vector x
        y = np.matmul(matrix, vec)
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
    return eig_val, vec

n = 5    # number of spins
d = 2**n  # matrix dimension dxd
b = 0.01  # magnetic field strength
t = 2.2   # temperature

# Evaluating matrix elements (Taken from weaver paper)
aa = np.exp((2 - b) / t )
bb = np.exp(-b/t)
cc = np.exp(-(2+b) / t)
aa_inv = np.exp(-(2 - b) / t )
bb_inv = np.exp(b/t)
cc_inv = np.exp((2+b) / t)

# Initialize transfer matrix
trans_mat = np.zeros((d,d))
# Populate matrix
for i in range((2**n)//2):
    # Populating the top half of the matrix
    if i < (2**n)//4:
        trans_mat[2*i][i] = aa
        trans_mat[2*i + 1][i] = bb
        trans_mat[2*i][i + 2**(n-1)] = aa_inv
        trans_mat[2*i + 1][i + 2**(n-1)] = bb_inv
    # Populating the bottom half of the matrix
    else:
        trans_mat[2*i][i] = bb
        trans_mat[2*i + 1][i] = cc
        trans_mat[2*i][i + 2**(n-1)] = bb_inv
        trans_mat[2*i + 1][i + 2**(n-1)] = cc_inv

# Max number of iterations (set by user)
max_iter = 200
# Tolerance (set by user)
tol = 10**-4
# Setting initial guess vector
init_vec = np.zeros(d)
init_vec[0] = 1

power_iter(max_iter, tol, trans_mat, init_vec)
