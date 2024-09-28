arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
result = test(arr, var0=2, var1=1)
expected = np.array([[2, 4], [7, 9]])
assert (result ==expected).all(), 'Test failed'