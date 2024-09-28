lst = [{'var1': 1, 'var2': 2, 'var3': 3}, {'var1': 4, 'var2': 5, 'var3': 6}]
var = 'var2'
expected_output = [{'var1': 1, 'var3': 3}, {'var1': 4, 'var3': 6}]
assert test(lst, var) == expected_output, 'Test failed'