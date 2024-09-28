lst0 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
expected_output = [['i', 'h', 'g'], ['f', 'e', 'd'], ['c', 'b', 'a']]
assert test(lst0) == expected_output, 'Test failed'