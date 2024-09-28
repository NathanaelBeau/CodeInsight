# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry']}, index=[1, 2, 3])
dict0 = {1: 'one', 3: 'three'}
expected_result =  pd.DataFrame({'fruit': ['apple', 'banana', 'cherry']}, index=['one', 2, 'three'])
result = test(df0, dict0)
assert result.equals(expected_result), 'Test failed'