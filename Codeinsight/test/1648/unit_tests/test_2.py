datetime_str = "2024-09-23"
result = test(datetime_str)
expected = pd.Timestamp("2024-09-23")
assert result == expected, 'Test failed'
