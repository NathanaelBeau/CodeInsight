df0 = pd.DataFrame({ ('A', 'A'): [1, 2], ('A', 'B'): [3, 4], ('B', 'A'): [5, 6], ('B', 'B'): [7, 8] })
str0 = 'A'
expected_result =  pd.DataFrame({ ('A', 'A'): [1, 2], ('B', 'A'): [5, 6] })
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'