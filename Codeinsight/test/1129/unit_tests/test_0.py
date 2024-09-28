var0 = {}
var1 = ['spam', 'ham']
var2 = 'dict3'
var3 = [5, 6]
expected_result =  {'dict3': {'spam': 5, 'ham': 6}}
result = test(var0, var1, var2, var3)
assert result == expected_result, 'Test failed'