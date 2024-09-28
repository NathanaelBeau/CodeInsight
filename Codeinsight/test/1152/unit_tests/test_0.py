lst0 = np.array([1, 2, 3, 4, 5, 100])
expected_result =  np.array([1, 2, 3, 4, 5])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'