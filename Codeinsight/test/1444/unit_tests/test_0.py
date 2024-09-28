df0 = pd.DataFrame({'Date': ['2023-09-01', '2023-09-02'], 'Time': ['12:00:00', '13:00:00']})
expected_result =  pd.to_datetime(['2023-09-01 12:00:00', '2023-09-02 13:00:00'])
result = test(df0, 'Date', 'Time')
assert all(result.values == expected_result.values), 'Test failed'