# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'apple', 'cherry', 'banana']})
expected_result =  pd.DataFrame({'fruit': ['apple', 'banana', 'apple', 'banana']})
result = test(df0, 'fruit').reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'