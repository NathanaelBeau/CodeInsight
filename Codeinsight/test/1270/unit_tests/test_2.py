arr0 = np.array([1, 2, 3])
var0 = [0, 1, 2]  # Remove all elements
result = test(arr0, var0)
expected = np.array([])
assert (result  == expected).all(), 'Test failed'