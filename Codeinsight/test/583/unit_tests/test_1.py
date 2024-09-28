# Test 3
lst0 = ["one", "two^", "three", "four&", "five"]
var0 = r'[\^&]'
expected_result =  ["one", "three", "five"]
assert test(lst0, var0) == expected_result, 'Test failed'