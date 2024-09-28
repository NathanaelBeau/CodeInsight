lst0 = ["0.1", "0.0.1", "0.0.0.1"]
expected_result =  ["0.0.0.1", "0.0.1", "0.1"]
result = test(lst0)
assert result == expected_result, 'Test failed'