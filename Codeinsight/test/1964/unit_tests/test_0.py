var0 = 'timestamp_column'
df0 = pd.DataFrame({'timestamp_column': [pd.Timestamp('2022-01-01 12:00:00'), pd.Timestamp('2022-01-02 14:00:00')]})
expected_result =  pd.DataFrame({'timestamp_column': [pd.Timestamp('2022-01-01').date(), pd.Timestamp('2022-01-02').date()]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'