arr0 = np.array([1, 2, 3])
items0 = [4, 5]
expected_result =  np.array([1, 2, 3, 4, 5])
result = test(arr0, items0)
assert np.array_equal(result, expected_result), 'Test failed'