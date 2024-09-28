df0 = pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f']})
Col0_name0 = 'Y'
expected_result =  pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['e', 'f', None]})
result = test(df0, Col0_name0)
assert result.equals(expected_result), 'Test failed'