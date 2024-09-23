arr1 = np.array([10, 20, 10, 40, 50])
old_val1 = 10
new_val1 = 0
expected_result =  np.array([0, 20, 0, 40, 50])
result = test(arr1, old_val1, new_val1)
assert np.array_equal(result, expected_result), 'Test failed'