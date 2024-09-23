lst0 = [(1, 'X', 'Y'), (1, 'Y', 'X'), (1, 'A', 'B'), (1, 'B', 'A')]
expected_output = [(1, 'X', 'Y')]
assert test(lst0) == expected_output, 'Test failed'