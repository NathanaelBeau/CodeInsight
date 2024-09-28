# Test case 1
arr0 = np.array([2, 3, 4])
value0 = 1
expected_result =  np.array([1, 2, 3, 4])
result = test(arr0, value0)
assert np.array_equal(result, expected_result), 'Test failed'