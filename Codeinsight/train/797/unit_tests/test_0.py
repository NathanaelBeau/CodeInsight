arr2 = np.array(['a', 'b', 'c', 'd'])
var2 = 3
expected_result =  np.array(['a', 'b', 'c'])
result = test(arr2, var2)
assert np.array_equal(result, expected_result), 'Test failed'