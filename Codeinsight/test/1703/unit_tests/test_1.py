df0 = pd.DataFrame({ 'A': [1, 1, 2, 2, 2], 'B': ['a', 'a', 'b', 'b', 'b'], 'C': [10, 20, 30, 40, 50] })
expected_output = pd.DataFrame({ 'A': [1, 2], 'B': ['a', 'b'], 'C': [20, 50] })
assert test(df0).values.tolist() == expected_output.values.tolist(), 'Test failed'