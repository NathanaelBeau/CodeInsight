# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
dict0 = {'a': 'alpha', 'b': 'beta'}
expected_result =  pd.DataFrame({'A': [1, 2, 3]}, index=['alpha', 'beta', 'c'])
result = test(df0, dict0)
assert result.equals(expected_result), 'Test failed'