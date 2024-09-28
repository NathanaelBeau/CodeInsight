df0 = pd.DataFrame({ ('A', 'A'): [1, 2], ('A', 'B'): [3, 4], ('B', 'A'): [5, 6], ('B', 'B'): [7, 8] })
str0 = 'B'
expected_result =  pd.DataFrame({ ('A', 'B'): [3, 4], ('B', 'B'): [7, 8] })
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'