str0 = "111000"
expected_output = np.array(['1', '1', '1', '0', '0', '0'])
assert (test(str0)  == expected_output).all(), 'Test failed'