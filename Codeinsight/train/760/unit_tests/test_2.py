df0 = pd.DataFrame({'M': [1.1, 2.2]})
df1 = pd.DataFrame({'M': [3.3, 4.4]})
expected_result =  pd.DataFrame({'M': [1.1, 2.2, 3.3, 4.4]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'