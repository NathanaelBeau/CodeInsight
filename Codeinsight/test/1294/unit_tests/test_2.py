df0 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
expected_result =  pd.DataFrame({'A': [10, 20, 100], 'B': [40, 50, 60]})
result = test(df0, 'A', 30, 100)
assert result.equals(expected_result), 'Test failed'