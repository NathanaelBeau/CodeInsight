# Unit Test 1
lst0 = [1, 2, 3]
lst1 = [4, 5, 6]
lst2 = [7, 8, 9]
expected_result =  [12, 15, 18]
result = test(lst0, lst1, lst2)
assert result == expected_result, 'Test failed'