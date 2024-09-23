df0 = pd.DataFrame({'A': [5, 6]})
df1 = pd.DataFrame({'B': [7, 8]})
expected_result =  pd.DataFrame({'A': [5, 5, 6, 6], 'B': [7, 8, 7, 8]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'