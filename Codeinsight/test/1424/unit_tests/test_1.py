series0 = pd.Series([10, 10, 10, 10])
expected_result =  pd.Series([25.0, 25.0, 25.0, 25.0])
result = test(series0)
assert result.equals(expected_result), 'Test failed'