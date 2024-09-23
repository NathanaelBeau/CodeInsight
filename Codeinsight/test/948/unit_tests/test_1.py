df0 = pd.DataFrame({'B': [4, 5, 6]})
var0 = 2
expected_output = pd.DataFrame({'B': [4, 5, 6, 4, 5, 6]})
result = test(df0, var0)
assert result['B'].tolist() == expected_output['B'].tolist(), 'Test failed'