arr0 = np.array([[[17, 18], [19, 20]], [[21, 22], [23, 24]]])
expected_result =  np.array([[17, 18], [19, 20], [21, 22], [23, 24]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'