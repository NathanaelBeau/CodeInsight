lst0 = ["1.2.5", "1.2.15", "1.2.3"]
expected_result =  ["1.2.3", "1.2.5", "1.2.15"]
result = test(lst0)
assert result == expected_result, 'Test failed'