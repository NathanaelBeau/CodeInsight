lst0 = [0, 0, 0]
lst1 = [1, 1, 1]
expected_result =  np.sqrt(3)
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'