df1 = pd.DataFrame({'col0': ['apple', 'banana', 'apple'], 'col1': [1, 2, 3]})
result_1 = test(df1, 'col0')
expected_1 = pd.DataFrame({'col0': [0, 1, 0], 'col1': [1, 2, 3]}).astype({'col0': 'int8'})
assert result_1.equals(expected_1), 'Test failed'