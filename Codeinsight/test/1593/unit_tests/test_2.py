# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane'], 'gender': ['M', 'F'], 'age': [30, 25], 'city': ['NY', 'LA']})
expected_result =  4
result = test(df0)
assert result == expected_result, 'Test failed'