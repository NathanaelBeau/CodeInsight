lst0 = [9, 10]
lst1 = [11, 12]
expected_result =  [(9, 11), (10, 12)]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'