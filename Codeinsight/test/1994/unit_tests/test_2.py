lst0 = ["apple", "banana", "cherry", "date"]
lst1 = ["date", "apple", "cherry", "banana"]
expected_result =  ["date", "apple", "cherry", "banana"]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'