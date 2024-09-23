arr0 = np.array([[3.2],
                 [1.5],
                 [2.8]])
expected_output = np.array([[1.5],
                            [2.8],
                            [3.2]])
assert (test(arr0)  == expected_output).all(), 'Test failed'