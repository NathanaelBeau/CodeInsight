arr0 = np.array([[10, 11], [12, 13]])
expected_result =  [np.array([10, 12]), np.array([11, 13])]
result = test(arr0)
assert all([np.array_equal(r, e) for r, e in zip(result, expected_result)]), 'Test failed'