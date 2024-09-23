lst0 = [[10], [20], [30], [40]]
lst1 = [11, 21, 31, 41]
expected_result =  [[10, 11], [20, 21], [30, 31], [40, 41]]
assert test(lst0, lst1) ==expected_result, 'Test failed'