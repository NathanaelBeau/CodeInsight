# Test case 2
arr0 = np.array([])
value0 = 10
expected_result =  np.array([10])
result = test(arr0, value0)
assert np.array_equal(result, expected_result), 'Test failed'