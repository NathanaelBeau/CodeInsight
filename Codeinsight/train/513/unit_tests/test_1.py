df0 = pd.DataFrame({'col_name': [4, 5], 'A': ['A3', 'A4']})
df1 = pd.DataFrame({'col_name': [4, 5], 'B': ['B3', 'B4']})
df2 = pd.DataFrame({'col_name': [4, 5], 'C': ['C3', 'C4']})
expected_result =  pd.DataFrame({'col_name': [4, 5], 'A': ['A3', 'A4'], 'B': ['B3', 'B4'], 'C': ['C3', 'C4']})
result = test(df0, df1, df2, 'col_name')
assert result.equals(expected_result), 'Test failed'