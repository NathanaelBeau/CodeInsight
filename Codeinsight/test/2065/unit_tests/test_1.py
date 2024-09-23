df0 = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})
df1 = pd.DataFrame({'Z': [7, 8, 9], 'W': [10, 11, 12]})
expected_output = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 8, 9], 'W': [10, 11, 12]})
assert test(df0, df1) .equals(expected_output), 'Test failed'