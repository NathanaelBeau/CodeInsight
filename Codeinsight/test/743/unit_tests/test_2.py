var0 = pd.DataFrame({'prod_type': [], 'price': []})
expected_result =  pd.DataFrame({'prod_type': [], 'price': []})
result = test(var0)
assert result.empty and expected_result.empty, 'Test failed'