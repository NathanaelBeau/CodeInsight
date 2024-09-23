var0 = [5, 6, 7, 8]
var1 = ['x', 'y', 'z', 'w']
var2 = [[100, 200], [300, 400], [500, 600], [700, 800]]
expected_output = [(5, 'x', 100, 200), (6, 'y', 300, 400), (7, 'z', 500, 600), (8, 'w', 700, 800)]
assert test(var0, var1, var2) ==expected_output, 'Test failed'