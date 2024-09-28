df2 = pd.DataFrame({'X': [10], 'Y': [20]})
expected_output2 = pd.DataFrame({'X': [10, 10, 10, 10, 10], 'Y': [20, 20, 20, 20, 20]})
assert test(df2).equals(expected_output2), 'Test failed'