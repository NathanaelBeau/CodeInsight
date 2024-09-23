var0 = "πρστυ"
expected_result =  "\\u03c0\\u03c1\\u03c3\\u03c4\\u03c5"
result = test(var0)
assert result == expected_result, 'Test failed'