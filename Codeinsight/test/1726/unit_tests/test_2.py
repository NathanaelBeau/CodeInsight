df0 = pd.DataFrame({'X': [], 'Y': []})
lst0 = [7, 8]
expected_result =  pd.DataFrame({'X': [7], 'Y': [8]})
result = test(df0.copy(), lst0)
assert result.equals(expected_result), 'Test failed'