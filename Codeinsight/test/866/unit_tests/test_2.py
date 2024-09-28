arr0 = np.array([[5, 10, 15, 20],
                   [25, 30, 35, 40],
                   [45, 50, 55, 60],
                   [65, 70, 75, 80]])
expected_output = np.array([[5, 10, 15, 20],
                              [25, 30, 35, 40],
                              [45, 50, 55, 60],
                              [65, 70, 75, 80]])
assert (test(arr0)  == expected_output).all(), 'Test failed'