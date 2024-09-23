df0 = pd.DataFrame({'common_column': [7, 8, 9], 'A': ['g', 'h', 'i']})
df1 = pd.DataFrame({'common_column': [9, 8, 7], 'B': ['r', 's', 't']})
expected_result =  pd.DataFrame({'common_column': [7, 8, 9], 'A': ['g', 'h', 'i'], 'B': ['t', 's', 'r']})
result = test(df0, df1, 'common_column')
assert result.equals(expected_result), 'Test failed'