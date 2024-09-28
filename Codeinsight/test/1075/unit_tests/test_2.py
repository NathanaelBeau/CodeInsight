df0 = pd.DataFrame({'var0': [['g', 'h'], ['g'], ['h', 'i']]})
expected_result =  pd.DataFrame({'g': [1, 1, 0], 'h': [1, 0, 1], 'i': [0, 0, 1]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'