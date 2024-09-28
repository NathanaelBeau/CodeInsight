lst0 = ["apple", "banana orange"]
expected_result =  [["apple"], ["banana", "orange"]]
result = test(lst0)
assert result == expected_result, 'Test failed'