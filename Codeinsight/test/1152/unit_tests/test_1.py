lst0 = [['a', 'bb'], 
        ['ccc', 'dddd'], 
        ['eeeee', 'f']]
expected_result =  ['eeeee', 'dddd']
result = test(lst0)
assert result == expected_result, 'Test failed'