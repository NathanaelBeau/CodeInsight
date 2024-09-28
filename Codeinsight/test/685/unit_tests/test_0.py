lst0 = [{"language": "en", "name": "John"}, {"language": "fr", "name": "Jean"}, {"language": "en", "name": "Doe"}]
expected_result =  [{"language": "en", "name": "John"}, {"language": "en", "name": "Doe"}, {"language": "fr", "name": "Jean"}]
result = test(lst0)
assert result == expected_result, 'Test failed'