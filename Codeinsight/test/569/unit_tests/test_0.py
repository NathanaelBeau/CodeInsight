var0 = 'group'
df0 = pd.DataFrame({'group': ['A', 'A', 'B', 'B', 'C'], 'value': [10, 20, 30, 40, 50]})
expected_result =  pd.DataFrame({'group': ['A', 'A', 'B', 'B', 'C'], 'value': [10, 20, 30, 40, 50], 'group_rank': [1, 2, 1, 2, 1]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'