# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', 'Doe']}, index=['first', 'second', 'third'])
dict0 = {'first': '1st', 'second': '2nd', 'third': '3rd'}
expected_result =  pd.DataFrame({'name': ['John', 'Jane', 'Doe']}, index=['1st', '2nd', '3rd'])
result = test(df0, dict0)
assert result.equals(expected_result), 'Test failed'