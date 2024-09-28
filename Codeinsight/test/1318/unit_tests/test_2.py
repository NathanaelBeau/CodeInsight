lst0 = [(53, 'x'), (53, 'y'), (53, 'z'), (10, 'w')]
expected_result =  [0, 1, 2]
result = test(lst0)
assert result == expected_result, 'Test failed'