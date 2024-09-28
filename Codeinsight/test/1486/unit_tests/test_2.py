dct0 = {"apple": "fruit", "carrot": "vegetable"}
dct1 = {"apple": "tech", "banana": "fruit"}
expected_result =  {"apple": "fruit"}
result = test(dct0, dct1)
assert result == expected_result, 'Test failed'