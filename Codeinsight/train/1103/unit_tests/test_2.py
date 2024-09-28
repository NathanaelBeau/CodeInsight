# Test 2
lst0 = [{'X': 10}, {'Y': 20, 'Z': 5}, {'X': 5, 'Z': 5}]
expected_result =  {'Y': 20, 'X': 15, 'Z': 10}
assert test(lst0) == expected_result, 'Test failed'