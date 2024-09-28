df0 = pd.DataFrame({ 'M': [10, 20], 'N': [20, 10] })
expected_result =  pd.DataFrame({ 'M': [10, 10], 'N': [20, 20] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'