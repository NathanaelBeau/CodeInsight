arr0 = np.array([[1, 2, 3],
                         [4, 2, 6],
                         [7, 8, 2]])
var0 = 2
result = test(arr0, var0)
expected = [(0, 1), (1, 1), (2, 2)]
assert (result == expected), 'Test failed'