df0 = pd.DataFrame({ 'A': [1, 2, 2, 4], 'B': [5, 5, 6, 6], 'C': [1, 2, 3, 4] })
expected_result =  pd.Series({'A': 3, 'B': 2, 'C': 4})
result = test(df0)
assert result.equals(expected_result), 'Test failed'