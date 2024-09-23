df0 = pd.DataFrame({ 'A': ['item4', 'item5', 'item6'], 'B': ['$11', '$21', '$31'], 'C': ['$6', '$16', '$26'] })
expected_result2 = pd.DataFrame({ 'A': ['item4', 'item5', 'item6'], 'B': [11.0, 21.0, 31.0], 'C': [6.0, 16.0, 26.0] })
result2 = test(df0)
assert result2.equals(expected_result2), 'Test failed'