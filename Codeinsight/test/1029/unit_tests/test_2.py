var0 = pd.DataFrame({'P': [10], 'Q': [20]})
expected_result =  pd.DataFrame({'P': [10], 'Q': [20], 'new_col': [0]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'