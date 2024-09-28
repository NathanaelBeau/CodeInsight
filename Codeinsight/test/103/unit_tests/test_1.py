arr0 = np.array([10, 20])
items0 = [30]
expected_result =  np.array([10, 20, 30])
result = test(arr0, items0)
assert np.array_equal(result, expected_result), 'Test failed'