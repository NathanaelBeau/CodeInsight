var0 = r'[0-9]+'
var1 = r'NUMBER'
str0 = "There are 10 apples and 5 oranges."
expected_output = "There are NUMBER apples and NUMBER oranges."
assert test(var0, var1, str0) ==expected_output, 'Test failed'