lst0 = [1, 2, 3, 4, 5]
expected_result =  pd.DataFrame({'Column_Name': [1, 2, 3, 4, 5]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'