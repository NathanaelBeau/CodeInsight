lst0 = [(1, True), (2, False), (3, True)]
var0 = 1
expected_result =  [True, False, True]
result = test(lst0, var0)
assert result == expected_result, 'Test failed'