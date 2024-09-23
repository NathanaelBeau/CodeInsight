lst0 = [{"language": "en", "name": "Doe"}, {"language": "en", "name": "John"}, {"language": "en", "name": "Jane"}]
expected_result =  [{"language": "en", "name": "Doe"}, {"language": "en", "name": "John"}, {"language": "en", "name": "Jane"}]
result = test(lst0)
assert result == expected_result, 'Test failed'