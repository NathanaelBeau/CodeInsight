df0 = pd.DataFrame({'W': ['c', 'd', 'c', 'd'], 'Z': [100, 200, 300, 400]})
column_name0 = 'W'
expected_result =  pd.DataFrame({'W': ['c', 'd'], 'Z': [400, 600]})
result = test(df0.copy(), column_name0)
assert result.equals(expected_result), 'Test failed'