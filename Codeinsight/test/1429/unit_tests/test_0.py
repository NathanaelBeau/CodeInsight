df0 = pd.DataFrame({ 'timestamp': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']), 'value': [1, 2, 3] })
str0 = 'timestamp'
time_interval0 = '2D'
expected_result =  pd.DataFrame({ 'timestamp': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']), 'value': [1.0, 1.5, 2.5] })
result = test(df0, str0, time_interval0)
assert result.equals(expected_result), 'Test failed'