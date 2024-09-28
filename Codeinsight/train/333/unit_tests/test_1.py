# Unit Test 3
df0 = pd.DataFrame({ 'P': [13, 14, 15], 'Q': [16, 17, 18] }, index=['one', 'two', 'three'])
expected_result =  pd.DataFrame({ 'P': [13, 14, 15], 'Q': [16, 17, 18] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'