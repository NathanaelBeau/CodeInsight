str0 = "2023-01-15 08:30:45.123456"
expected_output = datetime(2023, 1, 15, 8, 30, 45, 123456)
assert test(str0) ==expected_output, 'Test failed'