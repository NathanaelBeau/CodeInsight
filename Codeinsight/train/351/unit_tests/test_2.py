dict0 = {"male": "M", "female": "F"}
expected_result =  {"M": "male", "F": "female"}
result = test(dict0)
assert result == expected_result, 'Test failed'