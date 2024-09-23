var0 = "price: $50"
var1 = r"\$(\d+)"
expected_result =  "50"
assert test(var0, var1) == expected_result, 'Test failed'