test_array_4 = np.array([[3, 1]])
result_4 = test(test_array_4, sort_columns=[0])
expected_4 = np.array([[3, 1]])
assert np.array_equal(result_4, expected_4), 'Test failed'