lst0 = ["2.3.1", "2.3.0", "2.2.9"]
expected_result =  ["2.2.9", "2.3.0", "2.3.1"]
result = test(lst0)
assert result == expected_result, 'Test failed'