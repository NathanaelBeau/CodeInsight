# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry'], 'count': [5, 10, 15]})
condition = "fruit == 'apple' | count > 12"
expected_result =  pd.DataFrame({'fruit': ['apple', 'cherry'], 'count': [5, 15]})
result = test(df0, condition).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'