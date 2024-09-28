df0 = pd.DataFrame({'Date':['01-01-2022', '02-01-2022', '03-01-2022']})
expected_result =  pd.DataFrame({'Date': [pd.Timestamp('2022-01-01'), pd.Timestamp('2022-01-02'), pd.Timestamp('2022-01-03')]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'