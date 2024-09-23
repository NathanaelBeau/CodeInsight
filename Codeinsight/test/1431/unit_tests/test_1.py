df2 = pd.DataFrame({'B': ['apple', 'banana', 'apple', 'cherry']})
expected_result2 = pd.Series({'apple': 2, 'banana': 1, 'cherry': 1}, name='B')
result2 = test(df2, 'B')
assert result2.equals(expected_result2), 'Test failed'