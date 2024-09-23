mat0 = np.array([[10, 5], 
                 [2, 13]])
expected_result =  np.array([[0.66666667, 0.33333333], 
                            [0.13333333, 0.86666667]])
result = test(mat0)
assert np.allclose(result, expected_result), 'Test failed'