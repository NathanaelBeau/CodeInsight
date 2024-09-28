# Test 3
df0 = pd.DataFrame({ 'M': ['yes', 'no', 'yes', 'maybe', 'maybe'], 'N': ['no', 'yes', 'maybe', 'yes', 'no'] })
lst0 = ['M', 'N']
expected_result =  pd.DataFrame({ 'M': [2, 1, 2], 'N': [1, 2, 2] }, index=['maybe', 'no', 'yes'])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'