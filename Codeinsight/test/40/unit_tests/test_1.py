arr0 = np.array([10, 20, 30])
expected_result =  np.array([30, 20, 10])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'