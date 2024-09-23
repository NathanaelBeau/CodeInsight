lst0 = [True, False, True, False]
expected_result =  pd.DataFrame({'Column_Name': [True, False, True, False]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'