df0 = pd.DataFrame({'names': ['John,Mike', 'Jane,Susan'], 'scores': ['90,85', '88,78']})
var0 = 'names'
expected_result =  pd.Series(['John', 'Mike', 'Jane', 'Susan'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'