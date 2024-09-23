def test(matrix0):
    return np.all(np.linalg.eigvals(matrix0) > 0)

