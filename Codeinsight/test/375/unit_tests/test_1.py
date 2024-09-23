dict0 = {"key1": ["value1"]}
var0 = "key1"
var1 = "value2"
expected_output = {"key1": ["value1", "value2"]}
assert test(dict0,var0,var1) ==expected_output, 'Test failed'