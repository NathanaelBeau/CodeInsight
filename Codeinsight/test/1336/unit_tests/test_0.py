# Test 1
lst0 = ['apple', '\xe2', 'banana', '\xe2', 'cherry']
var0 = '\xe2'
expected_result =  ['apple', 'banana', 'cherry']
assert test(lst0, var0) == expected_result, 'Test failed'