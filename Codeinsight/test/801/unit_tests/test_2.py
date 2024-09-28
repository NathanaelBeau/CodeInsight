df0 = pd.DataFrame({'Code': ['A', 'B', 'C'], 'Desc': ['DescA', 'DescB', 'DescC']})
df1 = pd.DataFrame({'Code': ['X', 'Y', 'Z'], 'Info': ['InfoX', 'InfoY', 'InfoZ']})
var0 = 'Code'
expected_result =  pd.DataFrame({ 'Code': ['A', 'B', 'C', 'X', 'Y', 'Z'], 'Desc': ['DescA', 'DescB', 'DescC', None, None, None], 'Info': [None, None, None, 'InfoX', 'InfoY', 'InfoZ'] })
result = test(df0, df1, var0)
assert result.equals(expected_result), 'Test failed'