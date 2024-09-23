df0 = pd.DataFrame({'prod_type': [], 'price': []})
var0 = 'prod_type'
var1 = 'responsive'
expected_result =  pd.DataFrame({'prod_type': [], 'price': []})
result = test(df0, var0, var1)
assert result.empty and expected_result.empty, 'Test failed'