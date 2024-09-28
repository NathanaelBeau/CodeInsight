lst0 = ["apple", "banana", "cherry", "date"]
lst1 = ["cherry", "apple"]
n = 2
expected_result =  ["banana", "date"]
result = test(lst0, lst1, n)
assert result == expected_result, 'Test failed'