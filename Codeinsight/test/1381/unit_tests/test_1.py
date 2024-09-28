datetime0 = datetime.datetime(2015, 12, 31, 23, 59, 59)
expected_output = pd.Timestamp("2015-12-31 23:59:59")
assert test(datetime0) == expected_output, 'Test failed'