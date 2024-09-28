# Test 2
df0 = pd.DataFrame({'X': [10, 20], 'Y': [30, 40], 'Z': [50, 60]})
lst0 = ['X', 'Y', 'Z']
new_column_name = 'sum_XYZ'
expected_result =  pd.DataFrame({'X': [10, 20], 'Y': [30, 40], 'Z': [50, 60], 'sum_XYZ': [90, 120]})
result = test(df0, lst0, new_column_name)
assert result.equals(expected_result), 'Test failed'