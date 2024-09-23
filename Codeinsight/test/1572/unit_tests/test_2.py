arr = np.array([[1, 2, 1], [3, 1, 5], [1, 6, 1]])
result = test(arr, 1)
expected = np.array([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])
assert (result == expected).all(), 'Test failed'