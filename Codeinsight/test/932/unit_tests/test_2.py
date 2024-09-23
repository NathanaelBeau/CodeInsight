# Test 2
var0 = "The price is $100 not $50."
expected_result =  ['$100', '$50']
assert test(var0) == expected_result, 'Test failed'