mat0 = np.array([[10, 2], 
                 [1, 5]])
expected_result =  np.array([[0.83333333, 0.16666667], 
                            [0.16666667, 0.83333333]])
result = test(mat0)
assert np.allclose(result, expected_result), 'Test failed'