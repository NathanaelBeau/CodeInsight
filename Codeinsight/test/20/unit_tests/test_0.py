var0 = pd.DataFrame({'prod_type': ['mobile', 'desktop', 'tablet'], 'price': [100, 200, 300]})
expected_result =  pd.DataFrame({'prod_type': ['responsive', 'responsive', 'responsive'], 'price': [100, 200, 300]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'