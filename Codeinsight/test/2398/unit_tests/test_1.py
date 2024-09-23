df0 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'City': ['NY', 'LA', 'SF']})
var0 = 'Name'
expected_result =  pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['NY', 'LA', 'SF']})
result = test(df0, df1, var0)
assert result.equals(expected_result), 'Test failed'