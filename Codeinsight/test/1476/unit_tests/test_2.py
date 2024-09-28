var0 = 'city'
df0 = pd.DataFrame({'city': [None, 'PARIS', 'LONDON', 'BERLIN']})
expected_result =  pd.DataFrame({'city': [None, 'paris', 'london', 'berlin']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'