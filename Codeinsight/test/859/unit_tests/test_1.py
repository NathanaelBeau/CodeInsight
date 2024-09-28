arr0 = np.array([-5, -4, -3, -2, -1, 0])
condition = lambda x: x < 0
expected_result =  np.array([-5, -4, -3, -2, -1])
result = test(arr0, condition)
assert np.array_equal(result, expected_result), 'Test failed'