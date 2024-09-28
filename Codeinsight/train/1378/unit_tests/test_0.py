lst0 = [1, 2, 3, 4, 5]
expected_result =  1**2 + 2**2 + 3**2 + 4**2 + 5**2  # 55
result = test(lst0)
assert result == expected_result, 'Test failed'