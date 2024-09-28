dict0 = {"somekey": 1, "someotherkey": 2, "somekeyggg": 3}
lst0 = ["somekey", "someotherkey", "somekeyggg"]
expected_result =  True
assert test(dict0, lst0) == expected_result, 'Test failed'