lst0 = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
tpl0 = (10, 20, 30)
expected_output = [(10, 21, 32), (13, 24, 35), (16, 27, 38)]
assert test(lst0, tpl0) == expected_output, 'Test failed'