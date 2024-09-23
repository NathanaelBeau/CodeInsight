df0 = pd.DataFrame({'Date': ['2023-09-20', '2023-09-21'], 'Time': ['16:00:00', '17:00:00']})
expected_result =  pd.to_datetime(['2023-09-20 16:00:00', '2023-09-21 17:00:00'])
result = test(df0, 'Date', 'Time')
assert all(result.values == expected_result.values), 'Test failed'