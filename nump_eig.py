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
import generate
from numpy import linalg as la

n = 5   # number of spins
b = 0.01  # magnetic field strength
t = 2.2   # temperature

trans_mat = generate.tran_mat(n, b, t)
w, v = la.eig(trans_mat)
print("The dominant eigenvalue is:", max(w))
