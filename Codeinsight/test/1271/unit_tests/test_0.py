var0 = "Hello, World! This is an example string. Hello, again!"
var1 = "Hello"
expected_result =  ", World! This is an example string. , again!"
result = test(var0, var1)
assert result == expected_result, 'Test failed'