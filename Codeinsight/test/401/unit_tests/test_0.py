var0 = "Hello world Hello user Hello"
expected_result =  {("Hello", "world"): 1, ("world", "Hello"): 1, ("Hello", "user"): 1, ("user", "Hello"): 1}
assert test(var0) == expected_result, 'Test failed'