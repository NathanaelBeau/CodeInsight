df1 = pd.DataFrame({'X': [13, 14, 15]})
df2 = pd.DataFrame({'Y': [16, 17, 18]})
expected_result =  pd.DataFrame({'X': [13, 14, 15], 'Y': [16, 17, 18]})
result = test(df1, df2)
assert result.equals(expected_result), 'Test failed'