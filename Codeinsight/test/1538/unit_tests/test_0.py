var0 = "This is a {test} string with {multiple} placeholders."
expected_result =  ["test", "multiple"]
result = test(var0)
assert result == expected_result, 'Test failed'