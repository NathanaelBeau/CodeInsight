str0 = "hello"
var0 = "Hello World! hello again. hELLo thrice."
expected_result =  ["Hello", "hello", "hELLo"]
result = test(str0, var0)
assert result == expected_result, 'Test failed'