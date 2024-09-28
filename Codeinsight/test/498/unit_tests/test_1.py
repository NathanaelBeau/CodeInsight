df0 = pd.DataFrame({'common_column': [4, 5, 6], 'A': ['d', 'e', 'f']})
df1 = pd.DataFrame({'common_column': [4, 5, 6], 'B': ['u', 'v', 'w']})
expected_result =  pd.DataFrame({'common_column': [4, 5, 6], 'A': ['d', 'e', 'f'], 'B': ['u', 'v', 'w']})
result = test(df0, df1, 'common_column')
assert result.equals(expected_result), 'Test failed'