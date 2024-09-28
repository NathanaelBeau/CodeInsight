arr0 = np.array([[0.5, 0.5], [1.5, 1.5]])
expected_result =  np.array([[0.5, 0.5], [0.5, 0.5]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'