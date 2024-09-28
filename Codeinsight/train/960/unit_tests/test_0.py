df1 = pd.DataFrame({'A': [1, 2, 3, 3, 2]})
expected_result1 = pd.Series({1: 1, 2: 2, 3: 2}, name='A')
result1 = test(df1, 'A')
assert result1.equals(expected_result1), 'Test failed'