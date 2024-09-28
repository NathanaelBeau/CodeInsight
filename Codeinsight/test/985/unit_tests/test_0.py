lst0 = ['item100', 'item22', 'item3']
expected_result =  ['item3', 'item22', 'item100']
result = test(lst0)
assert result == expected_result, 'Test failed'