var0 = r'\s+'
var1 = "Hello   World"
expected_result =  ["Hello", "World"]
result = test(var0, var1)
assert result == expected_result, 'Test failed'