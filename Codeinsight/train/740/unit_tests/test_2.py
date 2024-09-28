# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane'], 'gender': ['M', 'F'], 'age': [30, 25]})
expected_result =  []
result = test(df0)
assert set(result) == set(expected_result), 'Test failed'