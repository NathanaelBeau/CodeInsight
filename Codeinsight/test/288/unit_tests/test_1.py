# Test 3
var0 = "one,two(three,four),five,six(seven)"
expected_result =  ["one", "two(three,four)", "five", "six(seven)"]
assert test(var0) == expected_result, 'Test failed'