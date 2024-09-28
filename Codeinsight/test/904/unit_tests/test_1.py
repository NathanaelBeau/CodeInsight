var0 = 'type'
df0 = pd.DataFrame({'type': ['x', 'y', 'x'], 'data': [4, 5, 6]})
expected_result =  {'x': pd.DataFrame({'type': ['x', 'x'], 'data': [4, 6]}), 'y': pd.DataFrame({'type': ['y'], 'data': [5]})}
result = test(df0, var0)
assert result['x'].equals(expected_result['x']) and result['y'].equals(expected_result['y']), 'Test failed'