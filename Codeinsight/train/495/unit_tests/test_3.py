lst0 = [1, 2, 3]
lst1 = [10, 20, 30]
expected_result =  [(1, 10), (2, 20), (3, 30)]
result = list(test(lst0, lst1))
assert result == expected_result, 'Test failed'