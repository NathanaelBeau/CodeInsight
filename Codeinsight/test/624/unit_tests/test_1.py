var0 = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']})
var1 = pd.DataFrame({'A': ['b', 'c', 'd'], 'B': ['e', 'f', 'g']})
expected_result =  pd.DataFrame({'A': ['a', 'b', 'c', 'd'], 'B': ['d', 'e', 'f', 'g']})
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'