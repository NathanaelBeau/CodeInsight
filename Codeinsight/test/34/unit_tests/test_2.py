# Test 3
df1 = pd.DataFrame({'name': ['John', 'Jane'], 'age': [30, 25]})
df2 = pd.DataFrame({'name': ['Doe', 'Smith'], 'age': [40, 35]})
lst0 = [df1, df2]
expected_result =  pd.DataFrame({'name': ['John', 'Jane', 'Doe', 'Smith'], 'age': [30, 25, 40, 35]})
result = test(lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'