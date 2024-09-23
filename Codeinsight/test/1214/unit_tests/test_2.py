lst0 = [(2, "apple"), (1, "bananas"), (3, "a")]
expected_result =  [(1, "bananas"), (2, "apple"), (3, "a")]
result = test(lst0)
assert result == expected_result, 'Test failed'