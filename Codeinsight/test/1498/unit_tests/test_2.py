# Test 3
columns = ['x', 'y']
index = 2
values = [10, 20]
expected_result =  pd.DataFrame({"x": [ 10], "y": [ 20]},index=[2])
result = test(columns, index, values)
assert result.equals(expected_result), 'Test failed'