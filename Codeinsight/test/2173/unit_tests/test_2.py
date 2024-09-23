arr0 = np.empty((0,2), int)
lst0 = [7, 8]
expected_result =  np.array([[7, 8]])
result = test(arr0, lst0)
assert np.array_equal(result, expected_result), 'Test failed'