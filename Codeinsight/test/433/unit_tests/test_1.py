lst0 = ["1", "2", "a", "3", "b"]
expected_result =  [1, 2, "a", 3, "b"]
result = test(lst0)
assert result == expected_result, 'Test failed'