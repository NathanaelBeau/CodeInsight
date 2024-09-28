df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [1, 2], 'B': [4, 5]})
assert test(df0).equals(expected_result), 'Test failed'