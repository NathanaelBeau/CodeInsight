var0 = b'\xc2\xa9'
expected_result =  '©'
result = test(var0)
assert result == expected_result, 'Test failed'