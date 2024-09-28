arr0 = np.array([[19, 20], [21, 22], [23, 24]])
lst0 = [1, 0, 1]
expected_result =  np.array([20, 21, 24])
result = test(arr0, lst0)
assert result.tolist() == expected_result.tolist(), 'Test failed'