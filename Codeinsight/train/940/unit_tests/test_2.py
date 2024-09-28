var0 = pd.DataFrame({'P': [11], 'Q': [12]}, index=['yellow'])
expected_result =  ['yellow']
result = test(var0)
assert result == expected_result, 'Test failed'