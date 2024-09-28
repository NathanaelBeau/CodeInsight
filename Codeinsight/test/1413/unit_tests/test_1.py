df0 = pd.DataFrame({'Date':['25-12-2019']})
expected_result =  pd.DataFrame({'Date': [pd.Timestamp('2019-12-25')]})
result = test(df0)
assert result .equals( expected_result), 'Test failed'