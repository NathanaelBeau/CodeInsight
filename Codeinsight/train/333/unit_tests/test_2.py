# Unit Test 2
df0 = pd.DataFrame({ 'X': [7, 8, 9], 'Y': [10, 11, 12] }, index=['a', 'b', 'c'])
expected_result =  pd.DataFrame({ 'X': [7, 8, 9], 'Y': [10, 11, 12] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'