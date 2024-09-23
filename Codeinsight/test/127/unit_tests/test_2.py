df3 = pd.DataFrame({ 'A': ['apple', 'apple', 'banana', 'apple', 'banana'], 'B': ['red', 'red', 'yellow', 'red', 'yellow'], 'C': [1, 10, 20, 5, 15] })
expected_result3 = pd.DataFrame({ 'A': ['apple', 'banana'], 'B': ['red', 'yellow'], 'C': [10, 20] })
result3 = test(df3)
assert result3.sort_values(by=['A', 'B']).reset_index(drop=True).equals(expected_result3.sort_values(by=['A', 'B']).reset_index(drop=True)), 'Test failed'