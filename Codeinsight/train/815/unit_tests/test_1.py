var0 = pd.DataFrame({ 'A': ['B', '1', '2'], 'C': ['D', '3', '4'] })
expected_result =  pd.DataFrame({ 'B': ['1', '2'], 'D': ['3', '4'] }, index=[1, 2])
result = test(var0)
assert result.equals(expected_result), 'Test failed'