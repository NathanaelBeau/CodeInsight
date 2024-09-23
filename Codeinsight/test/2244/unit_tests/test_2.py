df1 = pd.DataFrame({ 'A': ['apple', 'apple', 'banana', 'banana', 'cherry'], 'B': ['red', 'green', 'yellow', 'green', 'red'] })
key_columns1 = ['A']
expected_result1 = pd.Series([2, 2, 1], index=pd.Index(['apple', 'banana', 'cherry'], name='A'))
assert test(df1, key_columns1).equals(expected_result1), 'Test failed'