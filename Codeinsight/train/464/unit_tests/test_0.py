lst0 = [1, 2, 3]
lst1 = [4, 5, 6]
expected_result =  32  # 1*4 + 2*5 + 3*6
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'