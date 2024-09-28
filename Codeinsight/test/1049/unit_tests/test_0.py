arr0 = np.array([1, 2, 3, 4, 5])
lst0 = [3, 4]
expected_result =  np.array([False, False, True, True, False])
result = test(arr0, lst0)
assert np.array_equal(result, expected_result), 'Test failed'