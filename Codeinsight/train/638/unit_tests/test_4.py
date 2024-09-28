var0 = 2
var1 = 'machin'
var2 = [('John', 90, 'machin'), ('Jane', 75, 'truc'), ('Mike', '80', 'thing')]
expected_result =  [('John', 90, 'machin')]
result = test(var0, var1, var2)
assert result == expected_result, 'Test failed'