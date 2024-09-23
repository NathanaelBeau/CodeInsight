arr0 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
expected_output = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
assert (test(arr0)  == expected_output).all(), 'Test failed'