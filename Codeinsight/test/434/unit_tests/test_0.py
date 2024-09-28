# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
n = 2
expected_result =  pd.DataFrame({'A': [4, 5]})
result = test(df0, n).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'