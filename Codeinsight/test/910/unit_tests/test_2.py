df0 = pd.DataFrame({'name': ['Alice', 'Bob'], 'score': [85, 90]})
df1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'rank': [1, 2], 'score': [88, 91]})
var0 = 'name'
expected_result =  pd.DataFrame({'name': ['Alice', 'Bob'], 'score': [85, 90], 'rank': [1, 2]})
result = test(df0, df1, var0)
assert result.equals(expected_result), 'Test failed'