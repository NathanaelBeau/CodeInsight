dict0 = {"somekey": 1, "differentkey": 2, "somekeyggg": 3}
lst0 = ["somekey", "someotherkey", "somekeyggg"]
expected_result =  False
assert test(dict0, lst0) == expected_result, 'Test failed'