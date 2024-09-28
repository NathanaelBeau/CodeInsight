# Test 1
var0 = "I owe $money to $john."
expected_result =  ['$money', '$john']
assert test(var0) == expected_result, 'Test failed'