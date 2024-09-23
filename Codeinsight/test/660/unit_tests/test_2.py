df7 = pd.DataFrame({'P': [1, 3, 5], 'Q': [2, 4, 6]})
df8 = pd.DataFrame({'P': [2, 4, 6], 'Q': [1, 3, 5]})
lst2 = [df7, df8]
expected_result =  pd.DataFrame({'P': [1.5, 3.5, 5.5], 'Q': [1.5, 3.5, 5.5]})
result = test(lst2)
assert result.equals(expected_result), 'Test failed'