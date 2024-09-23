lst0 = np.array([7, 8, 9, 10, 11, 12, 13])
expected_result =  np.array([7, 8, 9, 11, 12, 13])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'