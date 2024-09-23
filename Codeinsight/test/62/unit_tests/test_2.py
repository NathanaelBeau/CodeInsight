dict0 = {'i': 100, 'j': 50, 'k': 25}
dict1 = {'i': 10, 'l': 5}
expected_result =  {'i': 10.0}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'