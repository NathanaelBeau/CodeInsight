df0 = pd.DataFrame({'G': [19, 20, 21], 'H': [22, 23, 24], 'I': [25, 26, 27]})
lst0 = ['I']
expected_result =  pd.DataFrame({'G': [19, 20, 21], 'H': [22, 23, 24]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'