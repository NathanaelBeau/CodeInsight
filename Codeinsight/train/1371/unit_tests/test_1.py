arr0 = np.empty((0,4), float)
lst0 = [1.1, 2.2, 3.3, 4.4]
expected_result =  np.array([[1.1, 2.2, 3.3, 4.4]])
result = test(arr0, lst0)
assert np.array_equal(result, expected_result), 'Test failed'