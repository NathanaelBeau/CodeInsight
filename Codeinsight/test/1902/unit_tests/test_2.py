# Test 3
arr0 = np.array([10, 20, 30, 40])
dict0 = {10: 'A', 20: 'B', 30: 'C'}
expected_result =  np.array(['A', 'B', 'C', np.nan])
result = test(arr0, dict0)
assert np.array_equal(result, expected_result), 'Test failed'