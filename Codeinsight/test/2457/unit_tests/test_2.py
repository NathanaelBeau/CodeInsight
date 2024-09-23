dict0 = { 'new YORK': 'Program1', 'California': 'Program2', 'Texas': 'Program3', 'Florida': 'Program4' }
expected_result =  ['Program1']
result = test(dict0)
assert result == expected_result, 'Test failed'