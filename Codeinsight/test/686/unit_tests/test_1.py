var0 = 1.2345e-50
expected_result =  "0.000000000000000000000000000000000000000000000000012345000000000000287"
result = test(var0)
assert result == expected_result, 'Test failed'