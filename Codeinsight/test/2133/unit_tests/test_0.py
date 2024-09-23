# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'new_C': [7, 8, 9], 'new_D': [10, 11, 12]})
result = test(df0, df1, ['new_C', 'new_D'], ['C', 'D'])
assert result.equals(expected_result), 'Test failed'