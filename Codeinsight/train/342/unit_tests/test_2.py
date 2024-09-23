str0 = "Another example with more than 100 characters: abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
expected_result =  "Another example with more than 100 characters: abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza"
result = test(str0)
assert result == expected_result, 'Test failed'