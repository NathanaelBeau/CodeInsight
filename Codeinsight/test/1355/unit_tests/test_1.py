functions = [lambda x: x*2, lambda x: x-1]
values = [5, 10, 15]
expected_output = [[10, 4], [20, 9], [30, 14]]
assert test(functions, values) == expected_output, 'Test failed'