df0 = pd.DataFrame({ 'apple': [10, 11, 12], 'kiwi': [13, 14, 15], 'banana': [16, 17, 18] })
str0 = 'a'
expected_result =  pd.DataFrame({ 'kiwi': [13, 14, 15] })
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'