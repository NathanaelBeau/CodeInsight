var0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['alpha', 'beta'])
expected_result =  ['alpha', 'beta']
result = test(var0)
assert result == expected_result, 'Test failed'