# Test 1
arr0 = np.array([1, 2, 3])
dict0 = {1: 'a', 2: 'b', 3: 'c'}
expected_result =  np.array(['a', 'b', 'c'])
result = test(arr0, dict0)
assert np.array_equal(result, expected_result), 'Test failed'