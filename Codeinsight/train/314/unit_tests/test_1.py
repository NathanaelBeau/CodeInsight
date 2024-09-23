arr0 = np.array([10.01, 20.99, 30.49, 40.51])
expected_result =  np.array([10, 20, 30, 40])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'