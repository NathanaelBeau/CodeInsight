df0 = pd.DataFrame({'common_column': [1, 2, 3], 'A': ['a', 'b', 'c']})
df1 = pd.DataFrame({'common_column': [1, 2, 3], 'B': ['x', 'y', 'z']})
expected_result =  pd.DataFrame({'common_column': [1, 2, 3], 'A': ['a', 'b', 'c'], 'B': ['x', 'y', 'z']})
result = test(df0, df1, 'common_column')
assert result.equals(expected_result), 'Test failed'