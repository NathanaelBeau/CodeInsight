df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
colA = 'A'
some_value = 2
colB = 'B'
new_value = 99
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 99, 6]})
result = test(df0, colA, some_value, colB, new_value)
assert result.equals(expected_result), 'Test failed'