df4 = pd.DataFrame({'X': [10, 20], 'Y': [30, 40]})
df5 = pd.DataFrame({'X': [20, 30], 'Y': [40, 50]})
df6 = pd.DataFrame({'X': [30, 40], 'Y': [50, 60]})
lst1 = [df4, df5, df6]
expected_result =  pd.DataFrame({'X': [20.0, 30.0], 'Y': [40.0, 50.0]})
result = test(lst1)
assert result.equals(expected_result), 'Test failed'