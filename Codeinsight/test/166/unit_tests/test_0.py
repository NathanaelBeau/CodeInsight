arr0 = np.array([1.2, 2.8, 3.5, 4.9])
expected_result =  np.array([1, 2, 3, 4])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'