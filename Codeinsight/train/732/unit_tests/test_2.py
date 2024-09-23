var0 = "Multiple;delimiters, in; this,string"
expected_result =  ["Multiple", "delimiters", "in", "this", "string"]
result = test(var0)
assert result == expected_result, 'Test failed'