# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry']})
df1 = pd.DataFrame({'color': ['red', 'yellow', 'red'], 'taste': ['sweet', 'sweet', 'sour']})
expected_result =  pd.DataFrame({'fruit': ['apple', 'banana', 'cherry'], 'fruit_color': ['red', 'yellow', 'red'], 'fruit_taste': ['sweet', 'sweet', 'sour']})
result = test(df0, df1, ['fruit_color', 'fruit_taste'], ['color', 'taste'])
assert result.equals(expected_result), 'Test failed'