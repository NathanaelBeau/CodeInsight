arr = np.array([[], []])
result = test(arr, var0=1, var1=1)
expected = np.array([[], []])
assert (result ==expected).all(), 'Test failed'