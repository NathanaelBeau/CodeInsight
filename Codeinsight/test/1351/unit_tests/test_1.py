var0 = "alpha beta gamma"
replacements = { "alpha": "one", "beta": "two", "gamma": "three" }
expected_result =  "one two three"
result = test(var0, replacements)
assert result == expected_result, 'Test failed'