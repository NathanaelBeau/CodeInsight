df0 = pd.DataFrame({'A': [10], 'B': [20]})
lst0 = [30, 40]
expected_result =  pd.DataFrame({'A': [10, 30], 'B': [20, 40]})
result = test(df0.copy(), lst0)
assert result.equals(expected_result), 'Test failed'