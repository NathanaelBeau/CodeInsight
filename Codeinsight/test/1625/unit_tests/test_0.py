var0 = "Hello, world! This is test123 string with - special_characters."
expected_result =  "Hello world This is test string with special characters"
result = test(var0)
assert result == expected_result, 'Test failed'