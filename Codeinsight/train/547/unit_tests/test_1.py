df0 = pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f']})
expected_output = ['0', '1', '2']
assert test(df0) ==expected_output, 'Test failed'