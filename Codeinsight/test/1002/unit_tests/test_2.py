arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
result = test(arr, var0=1, var1=0)
expected = np.array([[6, 7, 8, 9, 10]])
assert (result ==expected).all(), 'Test failed'