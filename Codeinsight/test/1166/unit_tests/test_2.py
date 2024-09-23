var0 = 'category'
df0 = pd.DataFrame({'category': ['cat1', 'cat1', 'cat2'], 'data': [5, 6, 7]})
expected_result =  pd.DataFrame({'category': ['cat1', 'cat1', 'cat2'], 'data': [5, 6, 7], 'group_rank': [1, 2, 1]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'