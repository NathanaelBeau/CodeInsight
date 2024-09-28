# Test 3
lst0 = [{'D': 2}, {'E': 6}, {'F': 10, 'D': 4}]
expected_result =  {'F': 10, 'E': 6, 'D': 6}
assert test(lst0) == expected_result, 'Test failed'