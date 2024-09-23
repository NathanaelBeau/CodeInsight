# Test 2
lst0 = [[1.2, 2.3], [3.4, 4.5], [5.6, 6.7]]
expected_result =  np.array([[1.2, 2.3], [3.4, 4.5], [5.6, 6.7]])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'