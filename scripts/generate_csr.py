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
    for i in range(d//2):
        col.append(i)
        col.append(i+4)
        col.append(i)
        col.append(i+4)
    row_ptr = [x for x in range(0,2*d,2)]
    return val, col, row_ptr
