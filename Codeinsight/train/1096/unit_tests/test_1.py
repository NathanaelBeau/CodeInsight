var0 = 'B'
df0 = pd.DataFrame({'A': ['7', '8', '9'], 'B': ['10', '11', '12']})
expected_result =  pd.DataFrame({'A': ['7', '8', '9'], 'B': [10, 11, 12]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'