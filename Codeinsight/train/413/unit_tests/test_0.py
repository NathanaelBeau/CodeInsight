functions = [lambda x: x**2, lambda x: x+2]
values = [1, 2, 3]
expected_output = [[1, 3], [4, 4], [9, 5]]
assert test(functions, values) == expected_output, 'Test failed'