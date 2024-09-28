# Test 2
ser0 = pd.Series([10, 20, 30], name='X')
ser1 = pd.Series([40, 50, 60], name='Y')
expected_result =  pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
result = test(ser0, ser1)
assert result.equals(expected_result), 'Test failed'