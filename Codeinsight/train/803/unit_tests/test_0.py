df0 = pd.DataFrame(columns=['Col1', 'Col2'])
expected_result =  pd.DataFrame(columns=['Col1', 'Col2'])
result = test(df0, 'Col1', ['men', 'rocks', 'mountains'])
assert result.equals(expected_result), 'Test failed'