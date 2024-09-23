df0 = pd.DataFrame({'A': ['1|2', '3|4', '5|6']})
expected_result =  pd.DataFrame({0: ['1', '3', '5'], 1: ['2', '4', '6']})
result = test(df0, 'A', var0='|')
assert result.equals(expected_result), 'Test failed'