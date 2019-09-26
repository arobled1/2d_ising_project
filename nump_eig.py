#=============================================================================80
# Description:
# Finds the dominant eigenvalue of the transfer matrix, as described in paper
# by Lim and Weare, using the _geev LAPACK routine, which is appropriately
# named np.eig().
# Python 3.7.4 was used.
# Paper: https://epubs.siam.org/doi/abs/10.1137/15M1040827
#===============================================================================
# Author: Alan Robledo
# Date: 9/26/19
#===============================================================================
# Output:
# For n = 5:
# Dominant eigenvalue is: (2.6132783525854255+0j)
#===============================================================================
import numpy as np
from numpy import linalg as la

n = 5   # number of spins
d = 2**n  # matrix dimension dxd
b = 0.01  # magnetic field strength
t = 2.2   # temperature

# Evaluating nonzero matrix elements (Taken from weaver paper)
aa = np.exp((2 - b) / t )
bb = np.exp(-b/t)
cc = np.exp(-(2+b) / t)
aa_inv = np.exp(-(2 - b) / t )
bb_inv = np.exp(b/t)
cc_inv = np.exp((2+b) / t)

# Initialize transfer matrix
trans_mat = np.zeros((d,d))
# Populate matrix
for i in range(d // 2):
    # Populating the top half of the matrix
    if i < d // 4:
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

w, v = la.eig(trans_mat)
print("The dominant eigenvalue is:", max(w))
