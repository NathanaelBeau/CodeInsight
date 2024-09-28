lst0 = ["OpenAI\tIs Great", "This\tIs Fun", "Tab\tSeparated"]
expected_result =  ["OpenAI", "This", "Tab"]
result = test(lst0)
assert result == expected_result, 'Test failed'