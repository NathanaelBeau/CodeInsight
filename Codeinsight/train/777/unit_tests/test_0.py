# Test 1
lst0 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
expected_result =  np.array(lst0)
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'