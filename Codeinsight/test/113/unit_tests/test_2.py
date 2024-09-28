dict0 = {'existing_dict': {'eggs': 7}}
expected_result =  {'existing_dict': {'eggs': 7}, 'dict3': {'spam': 5, 'ham': 6}}
result = test(dict0)
assert result == expected_result, 'Test failed'