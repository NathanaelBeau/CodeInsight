df0 = pd.DataFrame({'col': ['0', '1', '2', '3', '4','5']})
expected_output = pd.DataFrame({'col': [0, 1, 2, 3, 4,5]})
test(df0)
result = (df0['col'] == expected_output['col']).all()
assert result, 'Test failed'