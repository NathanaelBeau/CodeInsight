ser0 = pd.Series([10, 20, 30])
expected_result =  10
result = test(ser0)
assert result == expected_result, 'Test failed'