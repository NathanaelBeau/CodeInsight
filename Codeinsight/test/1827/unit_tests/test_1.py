# Test 3
df0 = pd.DataFrame({ 'col1': ['a', 'b', 'c'], 'col2': ['x', 'y', 'z'] })
lst0 = ['first', 'second']
expected_result =  pd.DataFrame({ 'first': ['a', 'b', 'c'], 'second': ['x', 'y', 'z'] })
assert test(df0.copy(), lst0).equals(expected_result), 'Test failed'