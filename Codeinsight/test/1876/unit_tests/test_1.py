pattern0 = r"ab"
var0 = "ababa"
expected_result =  ['ab', 'ab']
result = test(pattern0, var0)
assert result == expected_result, 'Test failed'