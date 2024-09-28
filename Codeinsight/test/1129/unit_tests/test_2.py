var0 = {'level1': {}}
var1 = ['a', 'b']
var2 = 'level1'
var3 = [1, 2]
expected_result =  {'level1': {'a': 1, 'b': 2}}
result = test(var0, var1, var2, var3)
assert result == expected_result, 'Test failed'