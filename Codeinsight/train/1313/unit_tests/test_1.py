# Test 2
rows = 3
columns = ['A', 'B']
expected_result =  pd.DataFrame(np.nan, index=range(3), columns=['A', 'B'])
result = test(rows, columns)
assert result.equals(expected_result), 'Test failed'