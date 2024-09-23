dict0 = {"item1": 1}
var0 = "item3"
var1 = 3
expected_result =  {"item1": 1, "item3": 3}
result = test(dict0, var0, var1)
assert result == expected_result, 'Test failed'