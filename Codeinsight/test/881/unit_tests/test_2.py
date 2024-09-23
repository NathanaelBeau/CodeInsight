var0 = 'category'
df0 = pd.DataFrame({ 'category': ['M', 'M', 'M'], 'values': [100, 200, 300] })
expected_result =  [
    pd.DataFrame({'category': ['M', 'M', 'M'], 'values': [100, 200, 300]}).reset_index(drop=True)
]
result = test(df0, var0)
assert all([res.equals(exp_res) for res, exp_res in zip(result, expected_result)]), 'Test failed'