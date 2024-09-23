series0 = pd.Series([5, 15, 30])
expected_result =  pd.Series([10.0, 30.0, 60.0])
result = test(series0)
assert result.equals(expected_result), 'Test failed'