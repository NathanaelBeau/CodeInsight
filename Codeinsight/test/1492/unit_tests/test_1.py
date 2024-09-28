# Test 2
df0 = pd.DataFrame({'A': ['apple', 'apple', 'banana'], 'B': [5, 10, 15]})
expected_result =  pd.DataFrame({'A': ['apple', 'banana'], 'B': [10, 15]})
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'