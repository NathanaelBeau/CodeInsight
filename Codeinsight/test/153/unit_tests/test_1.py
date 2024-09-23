lst0 = [[5, 6, 7], [8, 9]]
expected_result =  np.array([5, 6, 7, 8, 9])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'