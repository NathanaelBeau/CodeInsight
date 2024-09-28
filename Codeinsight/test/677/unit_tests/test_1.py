# Test 2
df0 = pd.DataFrame({ 'Name': ['John', 'Jane', 'John'], 'Score': [90, 85, 95] })
lst0 = ['Name', 'Score']
expected_result =  pd.DataFrame({ 'Name': ['Jane', 'John', 'John'], 'Score': [85, 90, 95] }, index=[1,0,2])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'