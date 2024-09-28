arr = np.array([1, 2, 3, 4, 5])
result = test(arr, 3)
expected = np.array([[2]])
assert (result == expected).all(), 'Test failed'