var0 = pd.DataFrame({'X': ['a', 'b'], 'Y': ['c', 'd']})
expected_result =  pd.DataFrame({'X': ['a', 'b'], 'Y': ['c', 'd'], 'new_col': [0, 1]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'