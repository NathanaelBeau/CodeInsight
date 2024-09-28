var0 = pd.DataFrame({'X': [5, 6, 7], 'Y': [8, 9, 10]}, index=['red', 'green', 'blue'])
expected_result =  ['red', 'green', 'blue']
result = test(var0)
assert result == expected_result, 'Test failed'