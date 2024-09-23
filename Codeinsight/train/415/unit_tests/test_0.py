df1 = pd.DataFrame({ 'A': [10, 20, 30], 'sum': [50, 100, 150] })
expected_result1 = pd.DataFrame({ 'A': [10, 20, 30], 'sum': [50, 100, 150], 'A_perc': [0.2, 0.2, 0.2] })
assert test(df1).equals(expected_result1), 'Test failed'