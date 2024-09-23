test_array_1 = np.array([[3, 1], [1, 2], [2, 3], [4, 0]])
result_1 = test(test_array_1, sort_column=0)
expected_1 = np.array([[1, 2], [2, 3], [3, 1], [4, 0]])
assert np.array_equal(result_1, expected_1), 'Test failed'