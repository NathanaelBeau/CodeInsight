df0 = pd.DataFrame({'X': ['a', 'b'], 'Y': ['c', 'd']})
df1 = pd.DataFrame({'X': ['e', 'f'], 'Y': ['g', 'h']})
expected_result =  pd.DataFrame({'X': ['a', 'b', 'e', 'f'], 'Y': ['c', 'd', 'g', 'h']})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'