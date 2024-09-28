var0 = 'group'
df0 = pd.DataFrame({'group': ['A', 'B', 'A'], 'value': [1, 2, 3]})
expected_result =  {'A': pd.DataFrame({'group': ['A', 'A'], 'value': [1, 3]}), 'B': pd.DataFrame({'group': ['B'], 'value': [2]})}
result = test(df0, var0)
assert result['A'].equals(expected_result['A']) and result['B'].equals(expected_result['B']), 'Test failed'