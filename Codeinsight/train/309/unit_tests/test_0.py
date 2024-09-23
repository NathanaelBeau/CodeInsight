arr0 = np.array([1, 2, 3, 5, 6, 8, 9, 10])
expected_result =  [np.array([1, 2, 3]), np.array([5, 6]), np.array([8, 9, 10])]
result = test(arr0)
assert all([np.array_equal(r, e) for r, e in zip(result, expected_result)]), 'Test failed'