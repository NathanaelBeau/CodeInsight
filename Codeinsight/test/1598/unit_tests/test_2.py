var0 = 'dates'
df0 = pd.DataFrame({'dates': [pd.Timestamp('2019-09-09 09:09:09')]})
expected_result =  pd.DataFrame({'dates': [pd.Timestamp('2019-09-09').date()]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'