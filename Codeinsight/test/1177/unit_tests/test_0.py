arr0 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
n0 = 3
expected_result =  [np.array([1, 2, 3, 4]), np.array([5, 6, 7]), np.array([8, 9, 10])]
result = test(arr0, n0)
assert all([np.array_equal(r, e) for r, e in zip(result, expected_result)]), 'Test failed'