var0 = [('apple', 1), ('banana', 2), ('cherry', 3), ('apple', 4)]
var1 = 'apple'
expected_result =  [0, 3]
result = test(var0, var1)
assert result == expected_result, 'Test failed'