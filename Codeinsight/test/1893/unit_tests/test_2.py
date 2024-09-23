df0 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'X': [100, 200, 300]})
expected_result =  pd.DataFrame({'X': [100, 200, 300]})
result = test(df0, 'X')
assert result.equals(expected_result), 'Test failed'