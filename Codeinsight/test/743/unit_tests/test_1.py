var0 = pd.DataFrame({'prod_type': [None, 'desktop', None], 'price': [50, 250, 350]})
expected_result =  pd.DataFrame({'prod_type': ['responsive', 'responsive', 'responsive'], 'price': [50, 250, 350]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'