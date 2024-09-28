# Test 2
df0 = pd.DataFrame({ 'Name': ['John', 'Jane', 'Jane', 'Doe'] }, index=['a', 'b', 'b', 'c'])
expected_result =  pd.DataFrame({ 'Name': ['John', 'Jane', 'Doe'] }, index=['a', 'b', 'c'])
result = test(df0)
assert result.equals(expected_result), 'Test failed'