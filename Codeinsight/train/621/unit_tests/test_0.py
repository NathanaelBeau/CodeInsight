var0 = "Hello\tworld!\nHello  again."
expected_result =  ["Hello", "world!", "Hello", "again."]
result = test(var0)
assert result == expected_result, 'Test failed'