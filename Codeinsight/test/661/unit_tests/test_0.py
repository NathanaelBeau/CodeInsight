var0 = 1
var1 = 10
var2 = 5
expected_result =  len(set(test(var0, var1, var2))) == var2
assert expected_result, 'Test failed'