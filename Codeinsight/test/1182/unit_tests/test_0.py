str0 = "Sunday 7"
var0 = '((?:Friday|Saturday)\s*\d{1,2})'
expected_output = ['Sunday 7']
assert test(str0, var0) ==expected_output, 'Test failed'