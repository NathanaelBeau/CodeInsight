df3 = pd.DataFrame({'X': ['a', 'b', 'c', 'd'], 'Y': ['e', 'f', 'g', 'h']})
expected_result3 = pd.DataFrame({'X': ['a', 'c', 'd'], 'Y': ['e', 'g', 'h']})
result3 = test(df3, 'X', 'b')
assert result3.equals(expected_result3), 'Test failed'