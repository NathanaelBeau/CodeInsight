lst0 = [(3, 'A', 'C'), (3, 'C', 'A'), (2, 'B', 'C'), (2, 'C', 'B'), (1, 'A', 'B'), (1, 'B', 'A')]
expected_output = [(3, 'A', 'C'), (2, 'B', 'C'), (1, 'A', 'B')]
assert test(lst0) == expected_output, 'Test failed'