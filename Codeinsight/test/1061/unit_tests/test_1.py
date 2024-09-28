str0 = "Monday 1, Tuesday 2, and Wednesday 3"
var0 = '((?:Friday|Saturday)\s*\d{1,2})'
expected_output = ['Monday 1, Tuesday 2, and Wednesday 3']
assert test(str0, var0) ==expected_output, 'Test failed'