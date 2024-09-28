df1 = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})
df2 = pd.DataFrame({'X': [0, 0, 0], 'Y': [0, 0, 0]})
expected_output = pd.DataFrame({'X': [0, 0, 0], 'Y': [0, 0, 0]})
assert test(df1, df2).equals(expected_output), 'Test failed'