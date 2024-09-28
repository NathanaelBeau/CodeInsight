arr0 = np.array([np.nan, 2.0, 3.0, np.nan, 5.0])
expected_output = np.array([2.0, 3.0, 5.0])
assert (test(arr0) ==expected_output).all(), 'Test failed'