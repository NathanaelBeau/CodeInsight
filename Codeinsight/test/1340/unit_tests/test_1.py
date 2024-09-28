df0 = pd.DataFrame({'prod_type': [None, 'desktop', None], 'price': [50, 250, 350]})
var0 = 'prod_type'
var1 = 'responsive'
expected_result =  pd.DataFrame({'prod_type': ['responsive', 'responsive', 'responsive'], 'price': [50, 250, 350]})
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'