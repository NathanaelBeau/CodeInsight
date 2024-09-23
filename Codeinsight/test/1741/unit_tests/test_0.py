df1 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['fruit', 'fruit', 'fruit']})
expected_result1 = pd.DataFrame({'A': ['apple', 'cherry'], 'B': ['fruit', 'fruit']})
result1 = test(df1, 'A', 'banana')
assert result1.equals(expected_result1), 'Test failed'