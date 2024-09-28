dict0 = {'apple': 100, 'banana': 200}
dict1 = {'apple': 4, 'banana': 50}
expected_result =  {'apple': 25.0, 'banana': 4.0}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'