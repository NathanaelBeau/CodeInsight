df0 = pd.DataFrame({'name': ['A', 'B'], 'value1': [1, 2]})
df1 = pd.DataFrame({'name': ['A', 'B'], 'value2': [3, 4]})
df2 = pd.DataFrame({'name': ['A', 'B'], 'value3': [5, 6]})
expected_result =  pd.DataFrame({'name': ['A', 'B'], 'value1': [1, 2], 'value2': [3, 4], 'value3': [5, 6]})
assert test(df0, df1, df2).equals(expected_result), 'Test failed'