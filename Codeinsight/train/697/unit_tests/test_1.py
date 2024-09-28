df2 = pd.DataFrame({'grade': ['70.9', '60.3', '50.1']})
var0 ='grade'
expected_result2 = pd.DataFrame({'grade': [70, 60, 50]})
result2 = test(df2, var0)
assert result2.equals(expected_result2), 'Test failed'