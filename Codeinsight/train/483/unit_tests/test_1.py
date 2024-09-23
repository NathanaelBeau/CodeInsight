# Test 2
df0 = pd.DataFrame({'sentence': ['I love python', 'Java is cool', 'C++ is powerful']})
column_name = 'sentence'
lst0 = ['python', 'C++']
expected_result =  pd.Series([True, False, True])
result = test(df0, column_name, lst0)
assert result.equals(expected_result), 'Test failed'