var0 = [1, 2, 3]
var1 = [True, False, True]
expected_result =  {1: True, 2: False, 3: True}
result = test(var0, var1)
assert result == expected_result, 'Test failed'