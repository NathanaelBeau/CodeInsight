lst0 = [(2, "apple"), (1, "banana"), (3, "cherry")]
expected_result =  [(1, "banana"), (2, "apple"), (3, "cherry")]
result = test(lst0)
assert result == expected_result, 'Test failed'