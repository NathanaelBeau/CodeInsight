def test(matrix0):
    try:
        np.linalg.cholesky(matrix0)
        return True
    except np.linalg.LinAlgError:
        return False
