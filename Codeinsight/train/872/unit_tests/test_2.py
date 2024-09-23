arr0 = np.array(['0', '-5.5', '10'])
expected_result =  np.array([0, -5.5, 10])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'