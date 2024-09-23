# Test 1
df0 = pd.DataFrame({ 'A': ['apple', 'banana', 'apple', 'apple'], 'B': ['red', 'yellow', 'red', 'green'] })
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({ 'A': [3., 1., np.nan, np.nan, np.nan], 'B': [np.nan, np.nan, 1., 2., 1.] }, index=['apple', 'banana', 'green', 'red', 'yellow'])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'