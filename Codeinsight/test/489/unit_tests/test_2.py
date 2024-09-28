# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', 'Doe'], 'age': [30, 25, 40]})
condition = "name != 'Doe' & age > 26"
expected_result =  pd.DataFrame({'name': ['John'], 'age': [30]})
result = test(df0, condition)
assert result.equals(expected_result), 'Test failed'