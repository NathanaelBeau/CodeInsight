arr0 = np.array(['apple', 'cherry'])
arr1 = np.array(['apple', 'banana', 'cherry', 'date'])
expected_result =  np.array([0, 2])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'