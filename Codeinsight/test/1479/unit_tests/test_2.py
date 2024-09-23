df0 = pd.DataFrame({'Col1': [0.5], 'Col2': [1.5]})
expected_result =  [0.5, 1.5]
result = test(df0)
assert result == expected_result, 'Test failed'