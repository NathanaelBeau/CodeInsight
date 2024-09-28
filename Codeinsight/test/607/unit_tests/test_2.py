var0 = pd.DataFrame({'name': ['John', 'Jane', 'Mike']})
lst0 = [30, 25, 40]
expected_result =  pd.DataFrame({'name': ['John', 'Jane', 'Mike'], 'new_column': [30, 25, 40]})
result = test(var0, lst0)
assert result.equals(expected_result), 'Test failed'