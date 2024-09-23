arr0 = np.array([[-2.3, -1.1, -0.5],
                 [-1.5, -4.2, -0.8],
                 [-2.8, -3.7, -1.9]])
expected_output = np.array([[-2.8, -3.7, -1.9],
                            [-2.3, -1.1, -0.5],
                            [-1.5, -4.2, -0.8]])
assert (test(arr0)  == expected_output).all(), 'Test failed'