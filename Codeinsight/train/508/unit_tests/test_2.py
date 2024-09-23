df0 = pd.DataFrame({ 'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e'], 'C': [10, 20, 30, 40, 50] })
expected_output = pd.DataFrame({ 'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e'], 'C': [10, 20, 30, 40, 50] })
assert test(df0).values.tolist() == expected_output.values.tolist(), 'Test failed'