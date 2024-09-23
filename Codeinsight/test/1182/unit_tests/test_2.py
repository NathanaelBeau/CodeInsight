str0 = "Sunday 1 and Monday 2 and Tuesday 3"
var0 = '((?:Friday|Saturday)\s*\d{1,2})'
expected_output = ['Sunday 1 and Monday 2 and Tuesday 3']
assert test(str0, var0) ==expected_output, 'Test failed'