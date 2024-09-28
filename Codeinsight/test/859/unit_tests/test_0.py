arr0 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
condition = lambda x: x > 5
expected_result =  np.array([6, 7, 8, 9])
result = test(arr0, condition)
assert np.array_equal(result, expected_result), 'Test failed'