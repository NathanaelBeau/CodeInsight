df0 = pd.DataFrame({'Date':['11-05-2020', '12-05-2020']})
expected_result =  pd.DataFrame({'Date': [pd.Timestamp('2020-05-11'), pd.Timestamp('2020-05-12')]})
result = test(df0)
assert result .equals( expected_result), 'Test failed'