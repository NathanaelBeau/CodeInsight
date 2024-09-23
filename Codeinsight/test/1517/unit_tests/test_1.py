lst0 = ["apple", "banana", "cherry"]
lst1 = ["banana", "cherry", "date"]
expected_result =  ["banana", "cherry"]
assert test(lst0, lst1) == expected_result or test(lst0, lst1) == ["cherry", "banana"], 'Test failed'