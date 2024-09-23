arr0 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
expected_output = np.array([3, 5, 7])
assert (test(arr0)  == expected_output).all(), 'Test failed'