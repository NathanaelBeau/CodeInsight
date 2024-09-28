var0 = pd.DataFrame({'  Value  ': [100, 200, 300]})
expected_result =  pd.DataFrame({'Value': [100, 200, 300]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'