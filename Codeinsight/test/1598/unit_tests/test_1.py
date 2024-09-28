var0 = 'time_data'
df0 = pd.DataFrame({'time_data': [pd.Timestamp('2020-05-05 10:10:10'), pd.Timestamp('2020-05-06 11:11:11')]})
expected_result =  pd.DataFrame({'time_data': [pd.Timestamp('2020-05-05').date(), pd.Timestamp('2020-05-06').date()]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'