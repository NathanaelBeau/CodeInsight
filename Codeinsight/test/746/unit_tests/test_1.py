# Test 2
columns = ['name', 'age']
index = 1
values = ["Alice", 25]
expected_result =  pd.DataFrame({"name": [ "Alice"], "age": [ 25]}, index=[1])
result = test(columns, index, values)
assert result.equals(expected_result), 'Test failed'