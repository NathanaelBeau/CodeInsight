var0 = pd.DataFrame({'MIXEDCase': [9, 10], 'ALREADYlower': [11, 12]})
expected_result =  pd.DataFrame({'mixedcase': [9, 10], 'alreadylower': [11, 12]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'