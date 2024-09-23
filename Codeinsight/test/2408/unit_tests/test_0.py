dct0 = {"a": 1, "b": 2, "c": 3}
dct1 = {"b": 4, "c": 5, "d": 6}
expected_result =  {"b": 2, "c": 3}
result = test(dct0, dct1)
assert result == expected_result, 'Test failed'