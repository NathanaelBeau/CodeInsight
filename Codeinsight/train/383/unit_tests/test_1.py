df2 = pd.DataFrame({'X': ['a', 'b'], 'Y': ['c', 'd']})
expected_result2 = [{'X': 'a', 'Y': 'c'}, {'X': 'b', 'Y': 'd'}]
result2 = test(df2)
assert result2 == expected_result2, 'Test failed'