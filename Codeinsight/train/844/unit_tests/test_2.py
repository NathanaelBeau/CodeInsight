df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'elephant', 'fox']})
df1 = pd.DataFrame({'A': ['apple'], 'B': ['dog']})
expected_result =  pd.DataFrame({'A': ['apple'], 'B': ['dog']})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'