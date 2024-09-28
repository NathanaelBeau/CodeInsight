# Test 2
df0 = pd.DataFrame({ 'old_name_1': [10, 20, 30], 'old_name_2': [40, 50, 60] })
lst0 = ['new_name_1', 'new_name_2']
expected_result =  pd.DataFrame({ 'new_name_1': [10, 20, 30], 'new_name_2': [40, 50, 60] })
assert test(df0.copy(), lst0).equals(expected_result), 'Test failed'