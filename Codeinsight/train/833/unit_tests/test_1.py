var0 = 'apple'
var1 = 'banana'
lst0 = ['apple', 'orange', 'apple']
expected_result =  ['banana', 'orange', 'banana']
assert test(var0, var1, lst0) == expected_result, 'Test failed'