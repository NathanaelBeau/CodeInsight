df5 = pd.DataFrame({'col0': ['banana', 'apple', 'apple', 'banana', 'orange'], 'col1': [5, 6, 7, 8, 9]})
result_5 = test(df5, 'col0')
expected_5 = pd.DataFrame({'col0': [1, 0, 0, 1, 2], 'col1': [5, 6, 7, 8, 9]}).astype({'col0': 'int8'})

# Check if the result matches the expected DataFrame
assert result_5.equals(expected_5),  'Test failed'