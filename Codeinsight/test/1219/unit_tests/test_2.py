var0 = pd.DataFrame({'C': [11, 12]})
expected_result =  pd.DataFrame({'C': [11, 12]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'