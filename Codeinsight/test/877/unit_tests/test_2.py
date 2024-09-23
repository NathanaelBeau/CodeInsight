var0 = 'category'
df0 = pd.DataFrame({'category': ['cat1', 'cat2', 'cat1'], 'info': [7, 8, 9]})
expected_result =  {'cat1': pd.DataFrame({'category': ['cat1', 'cat1'], 'info': [7, 9]}), 'cat2': pd.DataFrame({'category': ['cat2'], 'info': [8]})}
result = test(df0, var0)
assert result['cat1'].equals(expected_result['cat1']) and result['cat2'].equals(expected_result['cat2']), 'Test failed'