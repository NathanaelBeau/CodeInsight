var0 = pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f']})
expected_result =  pd.DataFrame({'X': ['c', 'b', 'a'], 'Y': ['f', 'e', 'd']}).reset_index(drop=True)
result = test(var0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'