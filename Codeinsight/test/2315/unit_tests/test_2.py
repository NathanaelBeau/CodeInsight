df0 = pd.DataFrame({'col_name': [6], 'A': ['A5']})
df1 = pd.DataFrame({'col_name': [6], 'B': ['B5']})
df2 = pd.DataFrame({'col_name': [6], 'C': ['C5']})
expected_result =  pd.DataFrame({'col_name': [6], 'A': ['A5'], 'B': ['B5'], 'C': ['C5']})
result = test(df0, df1, df2, 'col_name')
assert result.equals(expected_result), 'Test failed'