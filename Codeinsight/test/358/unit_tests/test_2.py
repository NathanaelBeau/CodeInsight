arr0 = np.array(['apple', 'banana', 'apple', 'cherry'])
expected_result =  np.array(['apple', 'banana', 'cherry'])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'