var0 = pd.DataFrame({'X': ['a', 'b', 'c']})
lst0 = ['d', 'e', 'f']
expected_result =  pd.DataFrame({'X': ['a', 'b', 'c'], 'new_column': ['d', 'e', 'f']})
result = test(var0, lst0)
assert result.equals(expected_result), 'Test failed'