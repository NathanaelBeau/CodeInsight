lst0 = [(10**18, 1), ("string", 2)]
expected_result =  False
result = test(lst0)
assert result == expected_result, 'Test failed'