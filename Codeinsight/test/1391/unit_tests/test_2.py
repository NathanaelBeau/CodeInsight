arr0 = np.array([np.nan, 1.0])
expected_output = np.array([1.0])
assert test(arr0) ==expected_output, 'Test failed'