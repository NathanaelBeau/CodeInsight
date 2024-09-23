mat0 = np.array([[15, 5], 
                 [2, 8]])
expected_result =  np.array([[0.75, 0.25], 
                            [0.2, 0.8]])
result = test(mat0)
assert np.allclose(result, expected_result), 'Test failed'