arr0 = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15]])
expected_output = np.array([5, 9, 13])
assert (test(arr0)  == expected_output).all(), 'Test failed'