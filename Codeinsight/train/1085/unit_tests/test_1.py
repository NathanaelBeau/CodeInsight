lst0 = [(1, 'X', 'Y'), (2, 'A', 'B'), (2, 'B', 'A'), (3, 'P', 'Q'), (3, 'Q', 'P')]
expected_output = [(1, 'X', 'Y'), (2, 'A', 'B'), (3, 'P', 'Q')]
assert test(lst0) == expected_output, 'Test failed'