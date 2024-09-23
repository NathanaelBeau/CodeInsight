lst0 = ['prefix45', 'prefix5', 'prefix400']
expected_result =  ['prefix5', 'prefix45', 'prefix400']
result = test(lst0)
assert result == expected_result, 'Test failed'