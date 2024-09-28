lst0 = [5, 6, 7]
expected_output = {((6, 7),), ((5, 6),), ((5, 7),), ((7, 5),), ((7, 6),), ((6, 5),)}
assert test(lst0) ==expected_output, 'Test failed'