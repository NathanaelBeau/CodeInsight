index0 = 1
dict0 = { "a": [3, 4, 5], "b": [1, 2, 3], "c": [6, 7, 8] }
expected_result =  {"b": [1, 2, 3], "a": [3, 4, 5], "c": [6, 7, 8]}
result = test(dict0, index0)
assert result == expected_result, 'Test failed'