lst0 = ['a', 'b', 'c', 'd', 'e']
expected_result =  pd.DataFrame({'Column_Name': ['a', 'b', 'c', 'd', 'e']})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'