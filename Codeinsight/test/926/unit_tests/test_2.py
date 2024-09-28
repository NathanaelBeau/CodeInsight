lst0 = [[['apple', 'banana'], 'cherry'], 'date']
expected_result =  ['apple', 'banana', 'cherry', 'date']
result = test(lst0)
assert result == expected_result, 'Test failed'