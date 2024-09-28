# Test 3
df0 = pd.DataFrame({ 'col1': [10, 20, 30], 'col2': [40, 50, 60], 'col3': [70, 80, 90] })
lst0 = ['col1', 'col3']
expected_result =  pd.DataFrame({ 'col1': [10, 20, 30], 'col3': [70, 80, 90] })
assert test(df0.copy(), lst0).equals(expected_result), 'Test failed'