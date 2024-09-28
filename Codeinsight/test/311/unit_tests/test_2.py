lst0 = [(10**18, 1), (10**19, 2), (10**20, "string")]
expected_result =  False
result = test(lst0)
assert result == expected_result, 'Test failed'