dict0 = {'dict1': {'name': 'Alice'}, 'dict2': {'city': 'NY', 'country': 'USA'}}
expected_result =  [['name'], ['city', 'country']]
assert test(dict0) == expected_result, 'Test failed'