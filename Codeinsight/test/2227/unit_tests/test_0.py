# Test 1
lst0 = ["apple", "orange@", "banana", "grape#"]
var0 = r'[@#]'
expected_result =  ["apple", "banana"]
assert test(lst0, var0) == expected_result, 'Test failed'