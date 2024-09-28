lst0 = ['alpha', 'beta', 'delta', 'gamma']
lst1 = [1, 1, 1, 1]
expected_result =  ['alpha', 'beta', 'delta', 'gamma']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'