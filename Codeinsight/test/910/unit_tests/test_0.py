# Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9] })
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
assert test(df0.copy(), lst0).equals(expected_result), 'Test failed'