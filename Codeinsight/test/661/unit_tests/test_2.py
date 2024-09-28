var0 = 1
var1 = 2
var2 = 1
expected_result =  len(set(test(var0, var1, var2))) == var2
assert expected_result, 'Test failed'