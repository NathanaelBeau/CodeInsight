arr0 = np.array([1, 2, 3, 4, 5, 6])
threshold0 = 3
expected_result =  np.array([4, 5, 6])
result = test(arr0, threshold0)
assert np.array_equal(result, expected_result), 'Test failed'