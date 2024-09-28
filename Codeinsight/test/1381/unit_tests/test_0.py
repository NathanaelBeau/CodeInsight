datetime0 = datetime.datetime(2020, 1, 1)
expected_output = pd.Timestamp("2020-01-01 00:00:00")
assert test(datetime0) == expected_output, 'Test failed'