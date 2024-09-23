df1_2 = pd.DataFrame({ 'A': [1, 2], 'B': [4, 5] }, index=['a', 'b'])
df2_2 = pd.DataFrame({ 'A': [7, 8, 9], 'B': [9, 10, 11] }, index=['a', 'b', 'c'])
expected_output2 = pd.DataFrame({ 'A': [4.0, 5.0, 9.0], 'B': [6.5, 7.5, 11.0] }, index=['a', 'b', 'c'])
assert test(df1_2, df2_2).equals(expected_output2), 'Test failed'