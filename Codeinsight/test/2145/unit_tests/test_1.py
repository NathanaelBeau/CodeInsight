lst0 = [range(5), range(5), range(5)]
expected_output = [(0, 0, 0),
 (1, 1, 1),
 (2, 2, 2),
 (3, 3, 3),
 (4, 4, 4)]
assert test(lst0) == expected_output, 'Test failed'