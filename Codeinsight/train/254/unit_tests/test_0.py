df1_1 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] }, index=['a', 'b', 'c'])
df2_1 = pd.DataFrame({ 'A': [7, 8], 'B': [9, 10] }, index=['a', 'b'])
expected_output1 = pd.DataFrame({ 'A': [4.0, 5.0, 3.0], 'B': [6.5, 7.5, 6.0] }, index=['a', 'b', 'c'])
assert test(df1_1, df2_1).equals(expected_output1), 'Test failed'