lst0 = [('P', 'y', 't', 'h', 'o', 'n'), ('R', 'o', 'c', 'k', 's')]
expected_result =  ['Python', 'Rocks']
result = test(lst0)
assert result == expected_result, 'Test failed'