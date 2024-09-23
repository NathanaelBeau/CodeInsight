lst0 = [1, [2, [3, [4, [5]]]]]
expected_result =  [1, 2, 3, 4, 5]
result = list(test(lst0))
assert result == expected_result, 'Test failed'