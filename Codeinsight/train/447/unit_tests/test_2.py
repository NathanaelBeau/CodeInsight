input_str = "OpenAI GPT-3"
expected_result =  [6, 5]
result = test(input_str)
assert result == expected_result, 'Test failed'