# Unit Test 1
df0 = pd.DataFrame({ ('A', 'first'): [1, 2], ('A', 'second'): [3, 4], ('B', 'first'): [5, 6] })
expected_result =  pd.DataFrame({ 'A first': [1, 2], 'A second': [3, 4], 'B first': [5, 6] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'