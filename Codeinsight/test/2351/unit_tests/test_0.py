arr0 = np.array([[0, 1], [1, 0]])
expected_result =  np.array([[0, 1], [1, 0]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'