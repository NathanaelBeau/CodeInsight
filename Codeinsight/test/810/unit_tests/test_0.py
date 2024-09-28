lst0 = [True, True, False, True, False]
var0 = ['BMW', 'VW', 'Volvo']
var1 = ['b', 'c']
expected_output = ['BMW', 'VW', 'b', 'Volvo', 'c']
assert test(lst0, var0, var1) == expected_output, 'Test failed'