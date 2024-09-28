var0 = 'x'
var1 = 'y'
lst0 = [1, 1, 2, 2, 1, 1]
lst1 = [1, 2, 2, 2, 2, 1]
expected_output = [0, 1, 2, 2, 1, 0]
assert (test(var0, var1, lst0,lst1) ==(expected_output)).all(), 'Test failed'