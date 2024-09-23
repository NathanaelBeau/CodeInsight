str0 = "This is a sample text that we are going to use to check if our function works correctly. It should trim this text to its first 100 characters."
expected_result =  str0[:100]
result = test(str0)
assert result == expected_result, 'Test failed'