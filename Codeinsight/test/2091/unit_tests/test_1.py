df2 = pd.DataFrame({'col0': ['red', 'green', 'blue', 'green'], 'col1': [1, 2, 3, 4]})
result_2 = test(df2, 'col0')
expected_2 = pd.DataFrame({'col0': [2, 1, 0, 1], 'col1': [1, 2, 3, 4]}).astype({'col0': 'int8'})
assert result_2.equals(expected_2),  'Test failed'