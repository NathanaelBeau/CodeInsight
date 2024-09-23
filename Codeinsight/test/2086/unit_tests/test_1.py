df0 = pd.DataFrame({ 'A': ['apple', 'banana', 'apple', 'banana'], 'B': [10, 20, 30, 40] })
expected_result =  pd.DataFrame({ ('B', 'sum'): {'apple': 40, 'banana': 60}, ('B', 'count'): {'apple': 2, 'banana': 2} })
result = test(df0)
assert result.equals(expected_result), 'Test failed'