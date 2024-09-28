var0 = "This is an example without non-English characters."
expected_result =  False
result = test(var0)
assert result == expected_result, 'Test failed'