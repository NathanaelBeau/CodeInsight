dict0 = { 'E': {'U': 9, 'V': 10}, 'F': {'U': 11, 'V': 12} }
expected_result =  pd.DataFrame({ 'E': {'U': 9, 'V': 10}, 'F': {'U': 11, 'V': 12} })
result = test(dict0)
assert result.equals(expected_result), 'Test failed'