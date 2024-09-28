lst0 = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert test(lst0) ==expected_output, 'Test failed'