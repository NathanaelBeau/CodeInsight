# Unit Test 2
df0 = pd.DataFrame({ ('X', 'alpha', 'one'): [7, 8], ('X', 'beta', 'two'): [9, 10], ('Y', 'gamma', 'three'): [11, 12] })
expected_result =  pd.DataFrame({ 'X alpha one': [7, 8], 'X beta two': [9, 10], 'Y gamma three': [11, 12] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'