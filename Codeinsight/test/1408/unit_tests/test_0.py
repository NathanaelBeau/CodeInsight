arr0 = np.array([1.0, 2.0, np.nan, 3.0, np.nan, 4.0])
expected_output = 4
assert test(arr0) ==expected_output, 'Test failed'