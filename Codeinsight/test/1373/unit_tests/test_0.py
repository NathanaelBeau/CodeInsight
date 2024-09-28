start0, end0, step0 = 0, 3, 1
start1, end1, step1 = 0, 2, 1
expected_result =  [np.array([[0, 0], [1, 1], [2, 2]]), np.array([[0, 1], [0, 1], [0, 1]])]
result = test(start0, end0, step0, start1, end1, step1)
assert all([np.array_equal(res, exp) for res, exp in zip(result, expected_result)]), 'Test failed'