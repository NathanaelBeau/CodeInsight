df0 = pd.DataFrame({'col': ['1', '2', '3', '4']})
expected_output = pd.DataFrame({'col': [1, 2, 3, 4]})
test(df0)
result = (df0['col'] == expected_output['col']).all()
assert result, 'Test failed'