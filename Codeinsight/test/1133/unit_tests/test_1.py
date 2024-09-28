lst0 = [(1, "apple"), (1, "a"), (1, "apples")]
expected_result =  [(1, "a"), (1, "apple"), (1, "apples")]
result = test(lst0)
assert result == expected_result, 'Test failed'