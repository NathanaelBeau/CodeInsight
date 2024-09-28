df5 = pd.DataFrame({'E': [17], 'F': [18]})
df6 = pd.DataFrame({'E': [19], 'F': [20]})
lst0 = [df5, df6]
expected_result =  pd.DataFrame({'E': [17, 19], 'F': [18, 20]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'