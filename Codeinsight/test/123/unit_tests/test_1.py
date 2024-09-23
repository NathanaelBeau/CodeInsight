lst0 = [-1, 0, 1]
lst1 = [1, 0, -1]
expected_result =  -2  # (-1)*1 + 0*0 + 1*(-1)
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'