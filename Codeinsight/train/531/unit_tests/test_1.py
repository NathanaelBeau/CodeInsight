df2 = pd.DataFrame({'X': ['apple', 'banana'], 'Y': ['red', 'yellow']})
expected_output2 = [{'index': 0, 'X': 'apple', 'Y': 'red'}, {'index': 1, 'X': 'banana', 'Y': 'yellow'}]
assert test(df2) == expected_output2, 'Test failed'