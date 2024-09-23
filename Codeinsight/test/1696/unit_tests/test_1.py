df0 = pd.DataFrame({'A': ['[apple]', '[banana]', '[cherry]'], 'B': ['[dog]', '[elephant]', '[fox]']})
expected_result =  pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'elephant', 'fox']})
result = test(df0)
assert result.equals(expected_result), 'Test failed'