# Test 1
lst0 = [{'A': 1, 'B': 2}, {'A': 3, 'B': 2, 'C': 1}]
expected_result =  {'A': 4, 'B': 4, 'C': 1}
assert test(lst0) == expected_result, 'Test failed'