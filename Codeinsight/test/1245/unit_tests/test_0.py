str0 = "abcdef"
char0 = '-'
expected_result =  "ab-cd-ef"
result = test(str0, char0)
assert result == expected_result, 'Test failed'