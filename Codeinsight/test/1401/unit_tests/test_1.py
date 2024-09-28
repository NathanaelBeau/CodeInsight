lst0 = ["apple", "banana", "cherry", "date", "elderberry"]
lst1 = [0, 2]
expected_result =  ["apple", "banana"]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'