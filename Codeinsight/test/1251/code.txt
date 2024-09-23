import numpy as np
def test(lst0, lst1):
    return sum(np.einsum('i,j->ij', lst0[i], lst1[i]) for i in range(len(lst0)))

