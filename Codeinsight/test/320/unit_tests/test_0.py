# Test 1
ser0 = pd.Series([1, 2, 3], name='A')
ser1 = pd.Series([4, 5, 6], name='B')
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(ser0, ser1)
assert result.equals(expected_result), 'Test failed'