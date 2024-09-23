str0 = "http://www.domain.com/?s=some&two=20"
var0 = "&"
expected_output = "http://www.domain.com/?s=some"
assert test(str0, var0) ==expected_output, 'Test failed'