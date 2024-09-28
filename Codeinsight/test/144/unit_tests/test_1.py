df2 = pd.DataFrame({ 'A': ['apple', 'apple', 'banana', 'banana', 'banana'], 'B': ['red', 'red', 'yellow', 'yellow', 'yellow'], 'C': [10, 15, 20, 25, 30] })
expected_result2 = pd.DataFrame({ 'A': ['apple', 'banana'], 'B': ['red', 'yellow'], 'C': [15, 30] })
result2 = test(df2)
assert result2.sort_values(by=['A', 'B']).reset_index(drop=True).equals(expected_result2.sort_values(by=['A', 'B']).reset_index(drop=True)), 'Test failed'