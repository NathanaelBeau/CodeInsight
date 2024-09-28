lst0 = [5.1, 2.2, 9.9, 7.8, 3.6]
var0 = 4
expected_output = [2, 3, 4, 0]
assert set(test(lst0, var0)) == set(expected_output), 'Test failed'