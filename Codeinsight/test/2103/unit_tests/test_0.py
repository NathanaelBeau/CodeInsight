var0 = 'B'
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
expected_result =  pd.DataFrame({'B': [4, 5, 6], 'A': [1, 2, 3], 'C': [7, 8, 9]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'