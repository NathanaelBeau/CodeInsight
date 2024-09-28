lst0 = [10, 20, 30]
lst1 = [0.1, 0.2, 0.3]
expected_result =  14.0  # 10*0.1 + 20*0.2 + 30*0.3
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'