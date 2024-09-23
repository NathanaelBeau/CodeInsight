str0 = "1999-12-31 23:59:59.999999"
expected_output = datetime(1999, 12, 31, 23, 59, 59, 999999)
assert test(str0) ==expected_output, 'Test failed'