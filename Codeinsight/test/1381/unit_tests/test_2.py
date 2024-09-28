datetime0 = datetime.datetime(2022, 5, 15, 15, 30, 45)
expected_output = pd.Timestamp("2022-05-15 15:30:45")
assert test(datetime0) == expected_output, 'Test failed'