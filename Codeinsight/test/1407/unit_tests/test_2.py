# Test case 3
arr0 = np.array([5, 6, 7, 8])
value0 = 4
expected_result =  np.array([4, 5, 6, 7, 8])
result = test(arr0, value0)
assert np.array_equal(result, expected_result), 'Test failed'