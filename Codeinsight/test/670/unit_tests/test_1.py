dict0 = { 'C': {'W': 5, 'Z': 6}, 'D': {'W': 7, 'Z': 8} }
expected_result =  pd.DataFrame({ 'C': {'W': 5, 'Z': 6}, 'D': {'W': 7, 'Z': 8} })
result = test(dict0)
assert result.equals(expected_result), 'Test failed'