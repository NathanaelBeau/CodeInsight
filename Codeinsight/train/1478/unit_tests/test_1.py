arr0 = np.array([[0, 0], [0, 0]])
expected_result =  np.empty((0, 2), int)
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'