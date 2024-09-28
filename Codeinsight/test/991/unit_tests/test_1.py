df0 = pd.DataFrame({'B': [7, 8, 9]})
arr0 = np.array([10, 11, 12])
expected_result =  pd.DataFrame({'B': [7, 8, 9], 'new_column': [10, 11, 12]})
result = test(df0, arr0)
assert result.equals(expected_result), 'Test failed'