df0 = pd.DataFrame({'P': ['c', 'a', 'b'], 'Q': ['f', 'd', 'e']}, index=[2, 0, 1])
expected_result =  pd.DataFrame({'P': ['a', 'b', 'c'], 'Q': ['d', 'e', 'f']}, index=[0, 1, 2])
result = test(df0)
assert result.equals(expected_result), 'Test failed'