df4 = pd.DataFrame({'Y': [True, False]})
df5 = pd.DataFrame({'Y': [False, True]})
expected_result =  pd.DataFrame({'Y': [True, False, False, True]})
result = test(df4, df5)
assert result.equals(expected_result), 'Test failed'