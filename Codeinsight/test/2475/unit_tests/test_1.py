df0 = pd.DataFrame({ 'X': ['banana', 'cherry'], 'Y': ['apple', 'date'] })
expected_result =  pd.DataFrame({ 'X': ['apple', 'cherry'], 'Y': ['banana', 'date'] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'