import numpy as np
def test(mat0):
    eigenvalues, eigenvectors = np.linalg.eig(mat0)
    idx = eigenvalues.argsort()[::-1]   
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:,idx]
    return eigenvalues, eigenvectors

