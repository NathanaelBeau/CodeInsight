test_array_2 = np.array([[3, 4], [1, 2], [2, 3], [4, 0]])
result_2 = test(test_array_2, sort_column=1)
expected_2 = np.array([[4, 0], [1, 2], [2, 3], [3, 4]])
assert np.array_equal(result_2, expected_2),  'Test failed'