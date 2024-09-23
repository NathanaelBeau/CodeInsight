df2 = pd.DataFrame({ 'X': ['cat', 'cat', 'dog', 'dog', 'bird'], 'Y': ['small', 'big', 'small', 'big', 'small'] })
key_columns2 = ['X', 'Y']
expected_result2 = pd.Series([1, 1, 1, 1, 1], index=pd.MultiIndex.from_tuples([('bird', 'small'), ('cat', 'big'), ('cat', 'small'), ('dog', 'big'), ('dog', 'small')], names=['X', 'Y']))
assert test(df2, key_columns2).equals(expected_result2), 'Test failed'