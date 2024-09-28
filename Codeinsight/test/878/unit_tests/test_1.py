df0 = pd.DataFrame({'P': [50, 100], 'Q': [150, 200]})
expected_result =  pd.DataFrame({'P': [0.0, 1.0], 'Q': [0.0, 1.0]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'