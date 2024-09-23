df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_result =  [[1, 3], [2, 4]]
assert test(df0) == expected_result, 'Test failed'