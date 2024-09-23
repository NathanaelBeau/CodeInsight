df2 = pd.DataFrame({ 'A': [5, 15, 25], 'sum': [25, 75, 125] })
expected_result2 = pd.DataFrame({ 'A': [5, 15, 25], 'sum': [25, 75, 125], 'A_perc': [0.2, 0.2, 0.2] })
assert test(df2).equals(expected_result2), 'Test failed'