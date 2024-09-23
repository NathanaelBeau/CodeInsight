arr0 = np.array([1, 2, 3, 4, 5])
old_val0 = 3
new_val0 = 99
expected_result =  np.array([1, 2, 99, 4, 5])
result = test(arr0, old_val0, new_val0)
assert np.array_equal(result, expected_result), 'Test failed'