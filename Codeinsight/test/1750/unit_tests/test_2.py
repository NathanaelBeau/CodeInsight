df0 = pd.DataFrame({'Col1': ['men', 'rocks', 'men', 'mountains'], 'Col2': [9, 10, 11, 12]})
expected_result3 = pd.DataFrame({'Col1': ['men', 'rocks', 'men', 'mountains'], 'Col2': [9, 10, 11, 12]})
result3 = test(df0, 'Col1', ['men', 'rocks', 'mountains'])
assert result3.equals(expected_result3), 'Test failed'