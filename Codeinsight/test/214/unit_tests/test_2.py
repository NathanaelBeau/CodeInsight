df2 = pd.DataFrame({'category': ['alpha', 'alpha', 'beta'], 'value': [20, 21, 22]})
col_name = 'category'
var2 = 1
result = test(df2, col_name, var2)
assert result['category'].value_counts().max() == var2, 'Test failed'