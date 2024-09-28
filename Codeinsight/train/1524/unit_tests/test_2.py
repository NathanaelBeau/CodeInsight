df3 = pd.DataFrame({'C1': ['a', 'b', 'c'], 'C2': ['d', 'e', 'f']})
expected_output3 = pd.DataFrame({ 'C1': ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c'], 'C2': ['d', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'f', 'f', 'f', 'f', 'f'] })
assert test(df3).equals(expected_output3), 'Test failed'