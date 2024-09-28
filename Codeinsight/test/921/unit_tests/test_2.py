arr2 = np.array([0, 0, 0, 0, 1, 1, 1])
var2 = 0
expected_output_2 = 4  # First value greater than 0 is 1
assert test(arr2, var2) == expected_output_2, 'Test failed'