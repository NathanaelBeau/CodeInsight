df0 = pd.DataFrame({'M': [10, 20, 30], 'N': [40, 50, 60]})
expected_result =  pd.DataFrame({'M': [10, 200, 30], 'N': [40, 50, 60]})
result = test(df0, 'M', 20, 200)
assert result.equals(expected_result), 'Test failed'