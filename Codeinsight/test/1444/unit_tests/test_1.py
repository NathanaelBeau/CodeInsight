df0 = pd.DataFrame({'Date': ['2023-09-10', '2023-09-11'], 'Time': ['14:00:00', '15:00:00']})
expected_result =  pd.to_datetime(['2023-09-10 14:00:00', '2023-09-11 15:00:00'])
result = test(df0, 'Date', 'Time')
assert all(result.values == expected_result.values), 'Test failed'