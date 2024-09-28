lst0 = []
expected_result =  True  # An empty list can be considered to satisfy the condition as it doesn't have any non-int element
result = test(lst0)
assert result == expected_result, 'Test failed'