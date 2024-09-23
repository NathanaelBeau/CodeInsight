df0 = pd.DataFrame({'var0': [['d'], ['e'], ['f']]})
expected_result =  pd.DataFrame({'d': [1, 0, 0], 'e': [0, 1, 0], 'f': [0, 0, 1]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'