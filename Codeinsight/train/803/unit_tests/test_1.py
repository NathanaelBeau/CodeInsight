df0 = pd.DataFrame({'Col1': ['sand', 'water', 'air'], 'Col2': [6, 7, 8]})
expected_result2 = pd.DataFrame(columns=['Col1', 'Col2'])
expected_result2['Col2'] = expected_result2['Col2'].astype('int64')  # Adjusting the data type
result2 = test(df0, 'Col1', ['men', 'rocks', 'mountains'])
assert result2.equals(expected_result2), 'Test failed'