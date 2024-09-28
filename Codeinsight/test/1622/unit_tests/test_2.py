df0 = pd.DataFrame({ 'col1': [1, 1, 1, 2], 'col2': [2, 2, 3, 3], 'col3': [4, 4, 5, 5] })
lst0 = ['col1', 'col2', 'col3']
expected_result =  ([1, 2, 3, 4, 5])
result = test(df0, lst0)
assert result == expected_result, 'Test failed'