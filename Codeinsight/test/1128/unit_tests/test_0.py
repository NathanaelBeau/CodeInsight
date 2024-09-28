dict0 = {"apple": 1, "banana": 2}
dict1 = {"cherry": 3}
expected_result =  {"apple": 1, "banana": 2, "cherry": 3}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'