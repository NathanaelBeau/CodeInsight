str0 = "name=John age=25 city=NY"
expected_result =  {'name': 'John', 'age': '25', 'city': 'NY'}
result = test(str0)
assert result == expected_result, 'Test failed'