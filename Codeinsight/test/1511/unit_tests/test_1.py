df2 = pd.DataFrame({'X': ['apple', 'banana'], 'Y': ['red', 'yellow']})
expected_output2 = [{'X': 'apple', 'Y': 'red'}, {'X': 'banana', 'Y': 'yellow'}]
assert test(df2) == expected_output2, 'Test failed'