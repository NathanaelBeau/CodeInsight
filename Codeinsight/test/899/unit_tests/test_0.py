var0 = 'category'
df0 = pd.DataFrame({ 'category': ['A', 'B', 'A', 'C', 'B'], 'values': [10, 20, 30, 40, 50] })
expected_result =  [
    pd.DataFrame({'category': ['A', 'A'], 'values': [10, 30]}).reset_index(drop=True),
    pd.DataFrame({'category': ['B', 'B'], 'values': [20, 50]}).reset_index(drop=True),
    pd.DataFrame({'category': ['C'], 'values': [40]}).reset_index(drop=True)
]
result = test(df0, var0)
assert all([res.equals(exp_res) for res, exp_res in zip(result, expected_result)]), 'Test failed'