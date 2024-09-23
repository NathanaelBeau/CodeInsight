var0 = "1999-12-31 23:59:59.999999"
expected_result3 = datetime(1999, 12, 31, 23, 59, 59, 999999)
assert test(var0) ==expected_result3, 'Test failed'