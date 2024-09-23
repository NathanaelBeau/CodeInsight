dict0 = {"name": "John", "age": 30}
dict1 = {"city": "New York", "job": "Engineer"}
expected_result =  {"name": "John", "age": 30, "city": "New York", "job": "Engineer"}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'