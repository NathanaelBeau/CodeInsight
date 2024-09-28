str0 = "hello"
var0 = "Hello World! hello again. hELLo thrice."
expected_result =  ["Hello", "hello", "hELLo"]
assert test(str0, var0) == expected_result, 'Test failed'