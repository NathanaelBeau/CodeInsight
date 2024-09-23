lst0 = [('D', 5.5), ('E', 4.0), ('F', 6.0), ('G', float('nan')), ('H', 3.0)]
expected_output = ('H', 3.0)
assert test(lst0) ==expected_output, 'Test failed'