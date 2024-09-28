df1 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
lst0 = ['X', 'Y']
expected_output1 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60], 'sum': [50, 70, 90]})
assert test(df1, lst0).equals(expected_output1), 'Test failed'