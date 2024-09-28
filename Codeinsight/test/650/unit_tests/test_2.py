arr0 = np.array([[7], [8], [9]])
expected_result =  [np.array([7, 8, 9])]
result = test(arr0)
assert all([np.array_equal(r, e) for r, e in zip(result, expected_result)]), 'Test failed'