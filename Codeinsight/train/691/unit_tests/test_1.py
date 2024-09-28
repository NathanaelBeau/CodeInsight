# Test 3
df0 = pd.DataFrame({ 'col1': [10], 'col2': [40] })
expected_result =  ['col1', 'col2']
assert test(df0) == expected_result, 'Test failed'