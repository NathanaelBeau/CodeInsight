df0 = pd.DataFrame({'prod_type': ['mobile', 'desktop', 'tablet'], 'price': [100, 200, 300]})
var0 = 'prod_type'
var1 = 'responsive'
expected_result =  pd.DataFrame({'prod_type': ['responsive', 'responsive', 'responsive'], 'price': [100, 200, 300]})
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'