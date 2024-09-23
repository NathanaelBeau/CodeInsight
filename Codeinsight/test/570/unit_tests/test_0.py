var0 = 'date_column'
df0 = pd.DataFrame({'date_column': ['2021-01-01', '2021-01-02', '2021-01-03']})
expected_result =  pd.DataFrame({'date_column': [pd.Timestamp('2021-01-01'), pd.Timestamp('2021-01-02'), pd.Timestamp('2021-01-03')]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'