series0 = pd.Series([1, 2, 3], name='D')
df0 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})
expected_result =  pd.DataFrame({'D': [1, 2, 3], 'A': [4, 5, 6], 'B': [7, 8, 9]})
result = test(series0, df0)
assert result.equals(expected_result), 'Test failed'