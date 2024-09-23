df0 = pd.DataFrame({ 'A': [None, 2, 3], 'B': [4, None, 6], 'C': [7, 8, None] })
lst0 = ['A', 'B', 'C']
expected_result =  pd.Series([4.0, 2.0, 3.0])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'