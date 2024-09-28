arr0 = np.array([[1, 2, 3], [4, 5, 6]])
expected_result =  np.array([[0.16666667, 0.33333333, 0.5], [0.26666667, 0.33333333, 0.4]])
result = test(arr0)
assert np.allclose(result, expected_result), 'Test failed'