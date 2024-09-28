lst0 = ["1.2.10", "1.2.2", "1.2.3"]
expected_result =  ["1.2.2", "1.2.3", "1.2.10"]
result = test(lst0)
assert result == expected_result, 'Test failed'