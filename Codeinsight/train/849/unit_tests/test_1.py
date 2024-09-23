df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [5, 25, 15], 'Z': [7, 8, 9]})
lst0 = ['X', 'Y', 'Z']
expected_result =  pd.DataFrame({'X': [10, 20, 30], 'Y': [5, 25, 15], 'Z': [7, 8, 9], 'max_value': [10, 25, 30]})
assert test(df0, lst0).equals(expected_result), 'Test failed'