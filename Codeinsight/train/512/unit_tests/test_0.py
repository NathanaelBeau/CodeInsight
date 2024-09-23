var0 = [1, 2, 3]
var1 = ['a', 'b', 'c']
var2 = [[10, 20], [30, 40], [50, 60]]
expected_output = [(1, 'a', 10, 20), (2, 'b', 30, 40), (3, 'c', 50, 60)]
assert test(var0, var1, var2) ==expected_output, 'Test failed'