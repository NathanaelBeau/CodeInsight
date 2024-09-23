# Test 1
columns = ['A', 'B']
index = 0
values = [1, 2]
expected_result =  pd.DataFrame({"A": [1], "B": [2]})
result = test(columns, index, values)
assert result.equals(expected_result), 'Test failed'