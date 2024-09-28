df0 = pd.DataFrame({ 'variable': ['P', 'P', 'Q', 'Q'], 'value': ['apple', 'banana', 'cherry', 'date'] })
expected_result =  pd.DataFrame({ 'P': ['apple', 'banana'], 'Q': ['cherry', 'date'] })
result = test(df0, 'variable', 'value')
assert result.equals(expected_result), 'Test failed'