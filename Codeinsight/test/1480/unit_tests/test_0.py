df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
lst0 = ['A', 'B']
expected_result =  np.array([[1, 4], [2, 5], [3, 6]])
result = test(df0, lst0)
assert np.array_equal(result, expected_result), 'Test failed'