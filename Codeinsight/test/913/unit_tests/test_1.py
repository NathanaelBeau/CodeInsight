var0 = pd.DataFrame({'A': [10, 20, 30, 40, 50], 'B': ['j', 'k', 'l', 'm', 'n']})
lst0 = [3, 6]
expected_result2 = pd.DataFrame(columns=['A', 'B'])
result2 = test(var0, lst0)
assert result2.empty and expected_result2.empty, 'Test failed'