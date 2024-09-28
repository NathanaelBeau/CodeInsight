df0 = pd.DataFrame({'col_name': [1, 2, 3], 'A': ['A0', 'A1', 'A2']})
df1 = pd.DataFrame({'col_name': [1, 2, 3], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'col_name': [1, 2, 3], 'C': ['C0', 'C1', 'C2']})
expected_result =  pd.DataFrame({'col_name': [1, 2, 3], 'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2'], 'C': ['C0', 'C1', 'C2']})
result = test(df0, df1, df2, 'col_name')
assert result.equals(expected_result), 'Test failed'