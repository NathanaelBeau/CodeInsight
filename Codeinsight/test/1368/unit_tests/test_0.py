str0 = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
str1 = 'abc'
expected_output = ['abc-123', 'abc-456']
assert test(str0, str1) ==expected_output, 'Test failed'