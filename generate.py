import numpy as np

def tran_mat(n, b, t):
    # matrix dimension dxd
    d = 2**n
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

    val = []
    for i in range(d//2):
        if i < d //4:
            val.append(aa)
            val.append(aa_inv)
            val.append(bb)
            val.append(bb_inv)
        else:
            val.append(bb)
            val.append(bb_inv)
            val.append(cc)
            val.append(cc_inv)
    col = []
    for i in range(d):
        col.append(i)
        col.append(i+4)
        col.append(i)
        col.append(i+4)
    row_ptr = [x for x in range(1,2*d,2)]
    # for i in range((2**n)//2):
    #     # Populating the top half of the matrix
    #     if i < (2**n)//4:
    #         trans_mat[2*i][i] = aa
    #         trans_mat[2*i + 1][i] = bb
    #         trans_mat[2*i][i + 2**(n-1)] = aa_inv
    #         trans_mat[2*i + 1][i + 2**(n-1)] = bb_inv
    #     # Populating the bottom half of the matrix
    #     else:
    #         trans_mat[2*i][i] = bb
    #         trans_mat[2*i + 1][i] = cc
    #         trans_mat[2*i][i + 2**(n-1)] = bb_inv
    #         trans_mat[2*i + 1][i + 2**(n-1)] = cc_inv
    return trans_mat
