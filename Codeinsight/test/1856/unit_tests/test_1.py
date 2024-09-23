var0 =0
var1 = 'John'
var2 = [('John', 30), ('Jane', 25), ('John', 35)]
expected_result =  [('John', 30), ('John', 35)]
result = test(var0, var1, var2)
assert result == expected_result, 'Test failed'