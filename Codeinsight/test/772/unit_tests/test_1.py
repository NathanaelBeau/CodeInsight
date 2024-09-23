start0, end0, step0 = 1, 4, 1
start1, end1, step1 = 2, 4, 1
expected_result =  [np.array([[1, 1], [2, 2], [3, 3]]), np.array([[2, 3], [2, 3], [2, 3]])]
result = test(start0, end0, step0, start1, end1, step1)
assert all([np.array_equal(res, exp) for res, exp in zip(result, expected_result)]), 'Test failed'