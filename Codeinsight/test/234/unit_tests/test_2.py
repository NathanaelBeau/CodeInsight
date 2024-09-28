lst0 = [-5, 0, 5]
lst1 = ['minus five', 'zero', 'five']
expected_result0 = tuple([-5, 0, 5])
expected_result1 = tuple(['minus five', 'zero', 'five'])
result0, result1 = test(lst0, lst1)
assert result0 == expected_result0 and result1 == expected_result1, 'Test failed'