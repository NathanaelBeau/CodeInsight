str0 = "Let's decode\\\\this"
expected_result =  "Let's decode\\this"
result = test(str0)
assert result == expected_result, 'Test failed'