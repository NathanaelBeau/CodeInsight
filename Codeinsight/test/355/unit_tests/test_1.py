df0 = pd.DataFrame({'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18]})
lst0 = ['D', 'E']
expected_result =  pd.DataFrame({'F': [16, 17, 18]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'