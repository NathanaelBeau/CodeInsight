df3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})
df4 = pd.DataFrame({'C': [13, 14], 'D': [15, 16]})
lst0 = [df3, df4]
expected_result =  pd.DataFrame({'C': [9, 10, 13, 14], 'D': [11, 12, 15, 16]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'