lst0 = ["apple", "banana", "cherry"]
lst1 = [5, 3, 8]
expected_result =  [("apple", 5), ("banana", 3), ("cherry", 8)]
assert test(lst0, lst1) == expected_result, 'Test failed'