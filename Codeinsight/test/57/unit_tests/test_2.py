ser0 = pd.Series([True, False, True])
expected_result =  True
result = test(ser0)
assert result == expected_result, 'Test failed'