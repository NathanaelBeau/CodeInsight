# Test 3
df0 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]})
lst0 = [0, 2]
expected_result =  pd.DataFrame({'Name': ['Bob', 'David'], 'Age': [30, 40]})
result = test(df0, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'