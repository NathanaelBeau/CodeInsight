df3 = pd.DataFrame({ 'A': [2, 4, 6], 'sum': [10, 20, 30] })
expected_result3 = pd.DataFrame({ 'A': [2, 4, 6], 'sum': [10, 20, 30], 'A_perc': [0.2, 0.2, 0.2] })
assert test(df3).equals(expected_result3), 'Test failed'