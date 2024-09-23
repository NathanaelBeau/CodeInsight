str0 = "Apricot"
lst0 = ["apple", "Banana", "Cherry"]
expected_result =  ["apple", "Apricot", "Banana", "Cherry"]
result = test(str0, lst0)
assert result == expected_result, 'Test failed'