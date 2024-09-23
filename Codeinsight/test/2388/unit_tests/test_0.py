df0 = pd.DataFrame({'A': [1, 2, 3]})
arr0 = np.array([4, 5, 6])
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'new_column': [4, 5, 6]})
result = test(df0, arr0)
assert result.equals(expected_result), 'Test failed'