var0 = np.array([[1, 2], [3, 4]])
str0 = "upper"
expected_output = np.array([[1, 2], [0, 4]])
assert np.array_equal(test(var0, str0), expected_output), 'Test failed'