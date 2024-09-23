lst0 = [(10, 20, 30), (100, 200, 300), (1000, 2000, 3000)]
tpl0 = (-5, -10, -15)
expected_output = [(5, 10, 15), (95, 190, 285), (995, 1990, 2985)]
assert test(lst0, tpl0) == expected_output, 'Test failed'