dict0 = {"somekey": 1, "someotherkey": 2, "extraKey": 3}
lst0 = ["somekey", "someotherkey"]
expected_result =  True
assert test(dict0, lst0) == expected_result, 'Test failed'