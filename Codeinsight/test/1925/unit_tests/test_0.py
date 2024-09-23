dict0 = {"item1": 1, "item2": 2}
expected_result =  {"item1": 1, "item2": 2, "item3": 3}
result = test(dict0)
assert result == expected_result, 'Test failed'