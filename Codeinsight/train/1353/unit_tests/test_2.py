lst0 = [range(10, 15), range(10, 15), range(10, 15)]
expected_output = [(10, 10, 10),
 (11, 11, 11),
 (12, 12, 12),
 (13, 13, 13),
 (14, 14, 14)]
assert test(lst0) == expected_output, 'Test failed'