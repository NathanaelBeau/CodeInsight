str0 = "Hello, world; how are you?"
expected_result =  ["Hello", "world", "how", "are", "you?"]
result = test(str0)
assert result == expected_result, 'Test failed'