var0 = 'flag'
var1 = [{'flag': True}, {'flag': False}, {'flag': True}, {'flag': True}]
expected_result =  3
result = test(var0, var1)
assert result == expected_result, 'Test failed'