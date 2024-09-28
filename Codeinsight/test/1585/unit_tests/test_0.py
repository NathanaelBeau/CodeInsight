df0 = pd.DataFrame({ 'Start Time': pd.to_datetime(['2021-01-01 08:00:00', '2021-01-01 09:00:00']), 'End Time': pd.to_datetime(['2021-01-01 10:00:00', '2021-01-01 11:30:00']) })
expected_result =  pd.DataFrame({ 'Hours': [2, 2], 'Minutes': [0, 30] })
result = test(df0, 'Start Time', 'End Time')
assert result.equals(expected_result), 'Test failed'