arr1 = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3])
var1 = -4
expected_output_1 = 2  # First value greater than -4 is -3
assert test(arr1, var1) == expected_output_1, 'Test failed'