arr0 = np.array([10, 20, 30, 40, 50])
condition = lambda x: x < 30
expected_result =  np.array([10, 20])
result = test(arr0, condition)
assert np.array_equal(result, expected_result), 'Test failed'