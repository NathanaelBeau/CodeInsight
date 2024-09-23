pattern0 = r"\d{3}"
var0 = "1234567890"
expected_result =  ['123', '234', '345', '456', '567', '678', '789', '890']
result = test(pattern0, var0)
assert result == expected_result, 'Test failed'