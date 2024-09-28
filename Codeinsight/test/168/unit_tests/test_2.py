# Test 2
var0 = "Special chars: @#&*! and non-ASCII: éáü"
expected_result =  "Special chars  and nonASCII "
assert test(var0) == expected_result, 'Test failed'