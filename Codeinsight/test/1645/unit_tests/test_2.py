arr2 = np.array(['a', 'b', 'c', 'd'])
old_val2 = 'b'
new_val2 = 'z'
expected_result =  np.array(['a', 'z', 'c', 'd'])
result = test(arr2, old_val2, new_val2)
assert np.array_equal(result, expected_result), 'Test failed'