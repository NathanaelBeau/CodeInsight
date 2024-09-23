dict0 = {}
var0 = "key1"
var1 = "value1"
var2 = "key2"
var3 = "value2"
expected_result =  {"key1": "value1", "key2": "value2"}
result = test(dict0, var0, var1, var2, var3)
assert result == expected_result, 'Test failed'