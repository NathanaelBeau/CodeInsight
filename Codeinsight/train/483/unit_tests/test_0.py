# Test 1
df0 = pd.DataFrame({'text': ['apple pie', 'banana bread', 'cherry tart']})
column_name = 'text'
lst0 = ['apple', 'banana']
expected_result =  pd.Series([True, True, False])
result = test(df0, column_name, lst0)
assert result.equals(expected_result), 'Test failed'