str0 = "100110"
expected_output = np.array(['1', '0', '0', '1', '1', '0'])
assert (test(str0)  == expected_output).all(), 'Test failed'