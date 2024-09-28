lst0 = [('A', 2.0), ('B', float('nan')), ('C', 1.5)]
expected_output = ('C', 1.5)
assert test(lst0) ==expected_output, 'Test failed'