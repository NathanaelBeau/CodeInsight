var0 = 'values'
df0 = pd.DataFrame({ 'category': ['X', 'Y', 'Z'], 'values': [5, 5, 6] })
expected_result =  [
    pd.DataFrame({'category': ['X', 'Y'], 'values': [5, 5]}).reset_index(drop=True),
    pd.DataFrame({'category': ['Z'], 'values': [6]}).reset_index(drop=True)
]
result = test(df0, var0)
assert all([res.equals(exp_res) for res, exp_res in zip(result, expected_result)]), 'Test failed'