lst0 = [("D", 7.5), ("E", float('nan')), ("F", 2.2)]
expected_output = 2.2
assert test(lst0) == expected_output, 'Test failed'