df0 = pd.DataFrame({'C': [7, 8, 9]})
var0 = 3
expected_output = pd.DataFrame({'C': [7, 8, 9, 7, 8, 9, 7, 8, 9]})
result = test(df0, var0)
assert result['C'].tolist() == expected_output['C'].tolist(), 'Test failed'