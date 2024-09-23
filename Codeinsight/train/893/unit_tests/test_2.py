df = pd.DataFrame({ 'col1': [2, 1, 3], 'col2': ['a', 'b', 'c'] })
expected_result =  pd.DataFrame({ 'col1': [1, 2, 3], 'col2': ['b', 'a', 'c'] })
result = test(df, 'col1', lambda x: x)
assert result.equals(expected_result), 'Test failed'