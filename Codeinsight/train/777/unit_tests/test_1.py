# Test 2
lst0 = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
expected_result =  np.array(lst0)
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'