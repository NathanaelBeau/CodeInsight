pattern0 = r"aa"
var0 = "aaaa"
expected_result =  ['aa', 'aa', 'aa']
result = test(pattern0, var0)
assert result == expected_result, 'Test failed'