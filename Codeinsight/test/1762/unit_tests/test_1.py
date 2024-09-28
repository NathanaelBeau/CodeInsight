s0 = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'orange', 'orange'])
expected_result =  pd.DataFrame({'value': ['orange', 'apple', 'banana'], 'count': [3, 2, 2]})
result = test(s0)
assert result.equals(expected_result), 'Test failed'