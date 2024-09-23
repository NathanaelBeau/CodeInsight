functions = [lambda x: x//2, lambda x: x%2]
values = [8, 13, 20]
expected_output = [[4, 0], [6, 1], [10, 0]]
assert test(functions, values) == expected_output, 'Test failed'