lst0 = [{"language": "es", "name": "Juan"}, {"language": "de", "name": "Hans"}, {"language": "it", "name": "Giovanni"}]
expected_result =  [{"language": "es", "name": "Juan"}, {"language": "de", "name": "Hans"}, {"language": "it", "name": "Giovanni"}]
result = test(lst0)
assert result == expected_result, 'Test failed'