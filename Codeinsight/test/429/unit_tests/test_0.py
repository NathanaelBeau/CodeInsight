df0 = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
expected_result =  2
assert test(df0) == expected_result, 'Test failed'