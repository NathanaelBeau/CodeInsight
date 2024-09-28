# Test 3
df0 = pd.DataFrame({ 'col1': ['a', 'b', 'c'], 'col2': ['x', 'y', 'z'] })
dict0 = {'col1': 'first', 'col2': 'second'}
expected_result =  pd.DataFrame({ 'first': ['a', 'b', 'c'], 'second': ['x', 'y', 'z'] })
assert test(df0.copy(), dict0).equals(expected_result), 'Test failed'