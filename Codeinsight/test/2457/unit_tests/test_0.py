dict0 = { 'New York': 'Program1', 'California': 'Program2', 'new york': 'Program3', 'Texas': 'Program4' }
expected_result =  ['Program1', 'Program3']
result = test(dict0)
assert result == expected_result, 'Test failed'