str0 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
expected_result =  str0[:100]
result = test(str0)
assert result == expected_result, 'Test failed'