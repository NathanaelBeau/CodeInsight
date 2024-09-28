df0 = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
var0 = 'NewLevel'
expected_result =  pd.DataFrame([[1, 2], [3, 4]], columns=pd.MultiIndex.from_tuples([(var0, 'A'), (var0, 'B')]))
result = test(var0, df0)
assert result.equals(expected_result), 'Test failed'