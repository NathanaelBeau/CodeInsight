# Test 2
df1 = pd.DataFrame({'fruit': ['apple', 'banana'], 'count': [5, 10]})
df2 = pd.DataFrame({'fruit': ['cherry', 'date'], 'count': [15, 20]})
lst0 = [df1, df2]
expected_result =  pd.DataFrame({'fruit': ['apple', 'banana', 'cherry', 'date'], 'count': [5, 10, 15, 20]})
result = test(lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'