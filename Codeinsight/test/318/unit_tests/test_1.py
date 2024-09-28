df0 = pd.DataFrame({'name': ['X'], 'value1': [7]})
df1 = pd.DataFrame({'name': ['X'], 'value2': [8]})
df2 = pd.DataFrame({'name': ['X'], 'value3': [9]})
expected_result =  pd.DataFrame({'name': ['X'], 'value1': [7], 'value2': [8], 'value3': [9]})
assert test(df0, df1, df2).equals(expected_result), 'Test failed'