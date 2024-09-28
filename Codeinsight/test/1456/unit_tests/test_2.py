arr0 = np.array([5.49, 6.51])
expected_result =  np.array([5.49, 6.51])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'