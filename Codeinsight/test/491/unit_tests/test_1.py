var0 = 'C'
df0 = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f'], 'C': ['g', 'h', 'i']})
expected_result =  pd.DataFrame({'C': ['g', 'h', 'i'], 'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'