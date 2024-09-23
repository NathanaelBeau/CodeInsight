var0 = 'A'
df0 = pd.DataFrame({'A': [30, 10, 20], 'B': [60, 40, 50]})
expected_result =  pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'