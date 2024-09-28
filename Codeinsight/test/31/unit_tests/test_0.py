var0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
str0 = "upper"
expected_output = np.array([[1, 2, 3], [0, 5, 6], [0, 0, 9]])
assert np.array_equal(test(var0, str0), expected_output), 'Test failed'