lst0 = [10, 20, 30]
var0 = 40
expected_result =  [10, 20, 30]  # 40 doesn't exist, so the list remains unchanged
assert test(lst0, var0) == expected_result, 'Test failed'