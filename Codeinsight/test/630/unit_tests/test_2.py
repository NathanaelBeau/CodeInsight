var0 = 'C'
df0 = pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18], 'C': [19, 20, 21]})
expected_result =  pd.DataFrame({'C': [19, 20, 21]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'