df0 = pd.DataFrame({'P': [10, 20, 30], 'Q': [40, 50, 60]})
Col0 = 'P'
expected_result =  pd.DataFrame({'P': [20, 30, None], 'Q': [40, 50, 60]})
result = test(df0, Col0)
assert result.equals(expected_result), 'Test failed'