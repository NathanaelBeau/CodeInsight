arr0 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])
expected_output = np.array([4, 7, 10, 13])
assert (test(arr0)  == expected_output).all(), 'Test failed'