df2 = pd.DataFrame({'X': ['a', 'b']})
df3 = pd.DataFrame({'X': ['c', 'd']})
expected_result =  pd.DataFrame({'X': ['a', 'b', 'c', 'd']})
result = test(df2, df3)
assert result.equals(expected_result), 'Test failed'