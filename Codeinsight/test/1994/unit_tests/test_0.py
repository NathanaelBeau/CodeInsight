lst0 = ["a", "b", "c", "d"]
lst1 = ["c", "d", "a", "b"]
expected_result =  ["c", "d", "a", "b"]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'