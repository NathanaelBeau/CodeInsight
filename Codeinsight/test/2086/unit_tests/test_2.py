df0 = pd.DataFrame({ 'A': ['x', 'y', 'z', 'x', 'y', 'z'], 'B': [100, 200, 300, 400, 500, 600] })
expected_result =  pd.DataFrame({ ('B', 'sum'): {'x': 500, 'y': 700, 'z': 900}, ('B', 'count'): {'x': 2, 'y': 2, 'z': 2} })
result = test(df0)
assert result.equals(expected_result), 'Test failed'