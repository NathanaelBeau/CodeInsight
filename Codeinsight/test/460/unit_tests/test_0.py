lst0 = [(1, 'apple'), (3, 'cherry'), (2, 'banana')]
expected_result =  [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
result = test(lst0)
assert result == expected_result, 'Test failed'