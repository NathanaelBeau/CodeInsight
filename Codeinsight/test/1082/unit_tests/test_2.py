arr0 = np.array([10, 20, 30, 40, 50])
threshold0 = 25
expected_result =  np.array([30, 40, 50])
result = test(arr0, threshold0)
assert np.array_equal(result, expected_result), 'Test failed'