# Test 3
df0 = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']})
expected_result =  pd.DataFrame({'name': ['David', 'Eve']})
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'