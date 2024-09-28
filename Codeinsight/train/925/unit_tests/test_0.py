lst0 = [(1, 'A', 'B'), (2, 'X', 'Y'), (2, 'Y', 'X'), (1, 'C', 'D'), (3, 'P', 'Q'), (3, 'Q', 'P')]
expected_output = [(1, 'A', 'B'), (2, 'X', 'Y'), (3, 'P', 'Q')]
assert test(lst0) == expected_output, 'Test failed'