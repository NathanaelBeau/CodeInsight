# Test 1
rows = 1
columns = ['A']
expected_result =  pd.DataFrame(np.nan, index=range(1), columns=['A'])
result = test(rows, columns)
assert result.equals(expected_result), 'Test failed'