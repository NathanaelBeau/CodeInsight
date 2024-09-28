var0 = "áéíóú"
expected_result =  "\\xe1\\xe9\\xed\\xf3\\xfa"
result = test(var0)
assert result == expected_result, 'Test failed'