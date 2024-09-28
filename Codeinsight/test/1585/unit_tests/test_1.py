df0 = pd.DataFrame({ 'Start Time': pd.to_datetime(['2021-01-01 08:30:00', '2021-01-01 09:45:00']), 'End Time': pd.to_datetime(['2021-01-01 10:15:00', '2021-01-01 10:55:00']) })
expected_result =  pd.DataFrame({ 'Hours': [1, 1], 'Minutes': [45, 10] })
result = test(df0, 'Start Time', 'End Time')
assert result.equals(expected_result), 'Test failed'