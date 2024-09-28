var0 = "foo bar baz"
replacements = { "foo": "apple", "bar": "banana", "baz": "cherry" }
expected_result =  "apple banana cherry"
result = test(var0, replacements)
assert result == expected_result, 'Test failed'