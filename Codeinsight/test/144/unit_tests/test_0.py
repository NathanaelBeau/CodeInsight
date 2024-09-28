df1 = pd.DataFrame({ 'A': ['apple', 'banana', 'apple', 'banana', 'apple'], 'B': ['red', 'yellow', 'red', 'yellow', 'red'], 'C': [1, 2, 3, 4, 5] })
expected_result1 = pd.DataFrame({ 'A': ['apple', 'banana'], 'B': ['red', 'yellow'], 'C': [5, 4] })
result1 = test(df1)
assert result1.sort_values(by=['A', 'B']).reset_index(drop=True).equals(expected_result1.sort_values(by=['A', 'B']).reset_index(drop=True)), 'Test failed'