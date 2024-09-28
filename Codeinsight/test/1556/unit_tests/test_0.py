str0 = "hello"
var0 = "Hello World! hello again. Hello thrice."
expected_result =  ["Hello", "hello", "Hello"]
assert test(str0, var0) == expected_result, 'Test failed'