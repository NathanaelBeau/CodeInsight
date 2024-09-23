series0 = pd.Series([5, 5, 15, 75])
expected_result =  pd.Series([5.0, 5.0, 15.0, 75.0])
result = test(series0)
assert result.equals(expected_result), 'Test failed'