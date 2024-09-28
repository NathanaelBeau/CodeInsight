# Test 3
lst0 = [[[1.1, 2.2], [3.3, 4.4]], [[5.5, 6.6], [7.7, 8.8]]]
expected_result =  np.array(lst0)
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'