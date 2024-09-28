var0 = [1, 2]
var1 = ['a', 'b']
var2 = [[10, 20], [30, 40]]
expected_output = [(1, 'a', 10, 20), (2, 'b', 30, 40)]
assert test(var0, var1, var2) ==expected_output, 'Test failed'