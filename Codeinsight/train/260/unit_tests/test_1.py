lst0 = [(7, 8, 9), (10, 11, 12)]
expected_result =  ([7, 10], [8, 11], [9, 12])
result = test(lst0)
assert result == expected_result, 'Test failed'