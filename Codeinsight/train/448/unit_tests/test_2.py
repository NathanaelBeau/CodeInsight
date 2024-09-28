var0 = 'B'
df0 = pd.DataFrame({'A': [300, 100, 200], 'B': [600, 400, 500]})
expected_result =  pd.DataFrame({'A': [100, 200, 300], 'B': [400, 500, 600]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'