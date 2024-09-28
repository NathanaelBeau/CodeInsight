var0 = "red blue yellow"
replacements = { "red": "a", "blue": "b", "yellow": "c" }
expected_result =  "a b c"
result = test(var0, replacements)
assert result == expected_result, 'Test failed'