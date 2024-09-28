arr0 = np.array([[7, 7, 7],
                         [7, 7, 7],
                         [7, 7, 7]])
var0 = 7
result = test(arr0, var0)
expected = [(0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2)]
assert (result == expected), 'Test failed'