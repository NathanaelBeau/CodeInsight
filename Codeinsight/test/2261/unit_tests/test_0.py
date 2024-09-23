var0 = r'\s+'
str0 = 'Hello   World'
expected_result =  ['Hello', 'World']
result = test(var0, str0)
assert result == expected_result, 'Test failed'