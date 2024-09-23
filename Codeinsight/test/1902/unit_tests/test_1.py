# Test 2
arr0 = np.array(['apple', 'banana', 'cherry'])
dict0 = {'apple': 'red', 'banana': 'yellow', 'cherry': 'dark red'}
expected_result =  np.array(['red', 'yellow', 'dark red'])
result = test(arr0, dict0)
assert np.array_equal(result, expected_result), 'Test failed'