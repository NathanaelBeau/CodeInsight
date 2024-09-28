var0 = 'OpenAI'
var1 = pd.Series(['OpenAI', 'GPT-3', 'OpenAI'])
expected_result =  pd.Series([np.nan, 'GPT-3', np.nan])
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'