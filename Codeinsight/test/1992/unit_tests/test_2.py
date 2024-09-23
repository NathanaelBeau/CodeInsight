test_array_3 = np.array([])
result_3 = test(test_array_3, sort_column=0)
expected_3 = np.array([])
assert np.array_equal(result_3, expected_3), 'Test failed'