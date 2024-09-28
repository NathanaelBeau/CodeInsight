var0 = 'group'
df0 = pd.DataFrame({'group': ['X', 'X', 'X', 'Y'], 'value': [1, 2, 3, 4]})
expected_result =  pd.DataFrame({'group': ['X', 'X', 'X', 'Y'], 'value': [1, 2, 3, 4], 'group_rank': [1, 2, 3, 1]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'