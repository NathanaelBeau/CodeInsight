arr0 = np.array([1, 2, 3, 4, 5, 6])
var0 = [1, 3]
result = test(arr0, var0)
expected = np.array([1, 3, 5, 6])
assert (result  == expected).all(), 'Test failed'