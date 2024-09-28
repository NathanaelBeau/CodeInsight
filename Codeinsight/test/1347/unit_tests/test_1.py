lst0 = [{"language": "es", "name": "Juan"}, {"language": "de", "name": "Hans"}, {"language": "it", "name": "Giovanni"}]
var0 = 'language'
var1 = 'en'
expected_result =  [{"language": "es", "name": "Juan"}, {"language": "de", "name": "Hans"}, {"language": "it", "name": "Giovanni"}]
result = test(lst0, var0, var1)
assert result == expected_result, 'Test failed'