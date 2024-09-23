df0 = pd.DataFrame([[5, 6], [7, 8]], columns=['X', 'Y'])
var0 = 'AnotherLevel'
expected_result =  pd.DataFrame([[5, 6], [7, 8]], columns=pd.MultiIndex.from_tuples([(var0, 'X'), (var0, 'Y')]))
result = test(var0, df0)
assert result.equals(expected_result), 'Test failed'