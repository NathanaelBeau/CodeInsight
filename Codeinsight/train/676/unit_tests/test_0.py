dict0 = {'a': 1, 'b': 1, 'c': 1}
expected_result =  set(dict0.keys())  
result = test(dict0)
assert result in expected_result, 'Test failed'