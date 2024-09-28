df1 = pd.DataFrame({'grade': ['100.5', '90.7', '80.2']})
var0 ='grade'
expected_result1 = pd.DataFrame({'grade': [100, 90, 80]})
result1 = test(df1, var0)
assert result1.equals(expected_result1), 'Test failed'