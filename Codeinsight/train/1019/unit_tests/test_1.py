df1 = pd.DataFrame({'X': ['apple', 'banana', 'cherry'], 'Y': [1, 2, 3]})
colA = 'X'
some_value = 'banana'
colB = 'Y'
new_value = 77
expected_result =  pd.DataFrame({'X': ['apple', 'banana', 'cherry'], 'Y': [1, 77, 3]})
result = test(df1, colA, some_value, colB, new_value)
assert result.equals(expected_result), 'Test failed'