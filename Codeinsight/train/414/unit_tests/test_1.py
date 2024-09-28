var0 = [('a', 1), ('b', 2), ('c', 1), ('d', 3)]
var1 = 'c'
expected_result =  [2]
result = test(var0, var1)
assert result == expected_result, 'Test failed'