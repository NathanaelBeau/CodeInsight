df0 = pd.DataFrame({ 'A': ['item7', 'item8', 'item9'], 'B': ['$12.2', '$22.2', '$32.2'], 'C': ['$7.2', '$17.2', '$27.2'] })
expected_result3 = pd.DataFrame({ 'A': ['item7', 'item8', 'item9'], 'B': [12.2, 22.2, 32.2], 'C': [7.2, 17.2, 27.2] })
result3 = test(df0)
assert result3.equals(expected_result3), 'Test failed'