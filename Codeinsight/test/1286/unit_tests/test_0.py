arr0 = np.array([1.0, 2.0, np.nan, 4.0, 5.0])
expected_output = np.array([1.0, 2.0, 4.0, 5.0])
assert (test(arr0)  == expected_output).all(), 'Test failed'