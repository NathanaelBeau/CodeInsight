arr0 = np.array([[1, 2],
                 [3, 4],
                 [5, 6],
                 [7, 8],
                 [9, 0]])
expected_output = np.array([[1, 2],
                            [3, 4],
                            [7, 8],
                            [9, 0]])
assert (test(arr0)  == expected_output).all(), 'Test failed'