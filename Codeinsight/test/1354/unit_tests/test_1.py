var0 = "Python is awesome. Python is dynamic."
var1 = "Python"
expected_result =  " is awesome.  is dynamic."
result = test(var0, var1)
assert result == expected_result, 'Test failed'