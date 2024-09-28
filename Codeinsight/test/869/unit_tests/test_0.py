lst0 = [("A", 5.5), ("B", 3.3), ("C", float('nan'))]
expected_output = 3.3
assert test(lst0) == expected_output, 'Test failed'