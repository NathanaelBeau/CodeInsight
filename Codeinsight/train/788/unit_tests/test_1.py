dict0 = {'apple': 'fruit', 'spinach': 'vegetable'}
dict1 = {'fruit': 'sweet', 'vegetable': 'salty'}
expected_result =  {'apple': 'sweet', 'spinach': 'salty'}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'