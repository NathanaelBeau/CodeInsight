dict0 = {"apple": "fruit", "broccoli": "vegetable"}
expected_result =  {"fruit": "apple", "vegetable": "broccoli"}
result = test(dict0)
assert result == expected_result, 'Test failed'