df0 = pd.DataFrame([[9, 10], [11, 12]], columns=['C', 'D'])
var0 = 'TopLevel'
expected_result =  pd.DataFrame([[9, 10], [11, 12]], columns=pd.MultiIndex.from_tuples([(var0, 'C'), (var0, 'D')]))
result = test(var0, df0)
assert result.equals(expected_result), 'Test failed'