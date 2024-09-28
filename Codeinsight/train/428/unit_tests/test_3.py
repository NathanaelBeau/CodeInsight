lst0 = ["orange", "apple", "banana", "apple"]
expected_result =  ["apple", "apple", "banana", "orange"]
result = test(lst0)
assert result == expected_result, 'Test failed'