df0 = pd.DataFrame({ 'C': [10, 20, 30], 'D': [40, 50, 60] }, index=['a', 'a', 'b'])
expected_output = pd.DataFrame({ 'C': [30, 30], 'D': [90, 60] }, index=['a', 'b'])
assert test(df0).equals(expected_output), 'Test failed'