lst0 = [{"language": "en", "name": "Doe"}, {"language": "en", "name": "John"}, {"language": "en", "name": "Jane"}]
var0 = 'language'
var1 = 'en'
expected_result =  [{"language": "en", "name": "Doe"}, {"language": "en", "name": "John"}, {"language": "en", "name": "Jane"}]
result = test(lst0, var0, var1)
assert result == expected_result, 'Test failed'