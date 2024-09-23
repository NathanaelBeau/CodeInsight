df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
column = 'Z'
value = [70, 80, 90]
expected_output = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60], 'Z': [70, 80, 90]})
result = test(df0.copy(), column, value)
assert result.equals(expected_output), 'Test failed'