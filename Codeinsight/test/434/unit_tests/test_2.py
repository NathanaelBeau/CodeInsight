arr0 = np.array([1.0, 2.0, 3.0, 4.0])
expected_result =  np.array([True, True, True, True])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'