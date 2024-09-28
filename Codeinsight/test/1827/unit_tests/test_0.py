str0 = "hello_world"
lst0 = [5]
expected_result =  ["hello", "_world"]
result = test(str0, lst0)
assert result == expected_result, 'Test failed'