start0, end0, step0 = 0, 4, 2
start1, end1, step1 = 1, 5, 2
expected_result =  [np.array([[0, 0], [2, 2]]), np.array([[1, 3], [1, 3]])]
result = test(start0, end0, step0, start1, end1, step1)
assert all([np.array_equal(res, exp) for res, exp in zip(result, expected_result)]), 'Test failed'