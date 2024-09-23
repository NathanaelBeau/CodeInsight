df0 = pd.DataFrame({'name': ['A', 'B', 'C'], 'value1': [10, 11, 12]})
df1 = pd.DataFrame({'name': ['A', 'B'], 'value2': [13, 14]})
df2 = pd.DataFrame({'name': ['A'], 'value3': [15]})
expected_result =  pd.DataFrame({'name': ['A'], 'value1': [10], 'value2': [13], 'value3': [15]})
assert test(df0, df1, df2).equals(expected_result), 'Test failed'