arr0 = np.empty((0, 3), int)
row0 = np.array([[1, 2, 3]])
expected_result =  np.array([[1, 2, 3]])
result = test(arr0, row0)
assert np.array_equal(result, expected_result), 'Test failed'