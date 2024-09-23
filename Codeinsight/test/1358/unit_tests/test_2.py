str0 = "banana"
lst0 = ["apple", "Banana", "cherry"]
expected_result =  ["apple", "Banana", "banana", "cherry"]
result = test(str0, lst0)
assert result == expected_result, 'Test failed'