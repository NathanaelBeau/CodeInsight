df0 = pd.DataFrame({'P': [5, 7, 9], 'Q': [1, 9, 3], 'R': [8, 2, 6]})
expected_result =  pd.Series(['R', 'Q', 'P'])
result = test(df0)
assert result.equals(expected_result), 'Test failed'