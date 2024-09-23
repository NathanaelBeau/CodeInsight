lst0 = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
expected_output = {1: 2, 2: 2, 3: 1}
assert test(lst0) ==expected_output, 'Test failed'