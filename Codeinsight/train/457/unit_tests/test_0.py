str0 = "a-1,b-2,c-3"
expected_result =  {'a': '1', 'b': '2', 'c': '3'}
result = test(str0)
assert result == expected_result, 'Test failed'