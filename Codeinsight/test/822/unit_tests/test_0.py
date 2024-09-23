df0 = pd.DataFrame({'A': ['a,b,c', 'd,e,f'], 'B': ['g,h,i', 'j,k,l']})
var0 = 'A'
expected_result =  pd.Series(['a', 'b', 'c', 'd', 'e', 'f'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'