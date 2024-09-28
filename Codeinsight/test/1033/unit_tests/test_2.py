lst0 = [10, 20, 30, 40]
lst1 = [100, 200, 300]
n = 2
expected_result =  [10, 20]
result = test(lst0, lst1, n)
assert result == expected_result, 'Test failed'