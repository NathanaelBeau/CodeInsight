arr0 = np.array([[3.2, 1.1, 2.3],
                 [1.5, 4.2, 0.8],
                 [2.8, 3.7, 1.9]])
expected_output = np.array([[1.5, 4.2, 0.8],
                            [2.8, 3.7, 1.9],
                            [3.2, 1.1, 2.3]])
assert (test(arr0)  == expected_output).all(), 'Test failed'