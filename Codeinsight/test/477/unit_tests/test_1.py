df0 = pd.DataFrame({ 'timestamp': pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-07']), 'value': [5, 10, 15] })
str0 = 'timestamp'
time_interval0 = '3D'
expected_result =  pd.DataFrame({ 'timestamp': pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-07']), 'value': [5.0, 10.0, 12.5] })
result = test(df0, str0, time_interval0)
assert result.equals(expected_result), 'Test failed'