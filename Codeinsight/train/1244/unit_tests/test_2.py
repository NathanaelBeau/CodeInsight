# Test 3
df0 = pd.DataFrame({'M': ['10.01$11.49', '11.99$12.99', '13.50$14.50']})
var0 = 'M'
var1 = 'Price1'
var2 = 'Price2'
var3 = '$'
expected_result =  pd.DataFrame({'M': ['10.01$11.49', '11.99$12.99', '13.50$14.50'], 'Price1': ['10.01', '11.99', '13.50'], 'Price2': ['11.49', '12.99', '14.50']})
result = test(df0, var0, var1, var2, var3)
assert result.equals(expected_result), 'Test failed'