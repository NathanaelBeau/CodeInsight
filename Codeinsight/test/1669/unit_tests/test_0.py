dict0 = { 'A': {'X': 1, 'Y': 2}, 'B': {'X': 3, 'Y': 4} }
expected_result =  pd.DataFrame({ 'A': {'X': 1, 'Y': 2}, 'B': {'X': 3, 'Y': 4} })
result = test(dict0)
assert result.equals(expected_result), 'Test failed'