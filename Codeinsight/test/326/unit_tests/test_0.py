lst0 = [['apple', 'banana'], 
        ['cherry', 'date'], 
        ['eggplant', 'fig']]
expected_result =  ['eggplant', 'banana']
result = test(lst0)
assert result == expected_result, 'Test failed'