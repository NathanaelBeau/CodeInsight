df0 = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'Dave'], 'status': ['active', 'inactive', 'active', 'banned']})
col0 = 'status'
str0 = 'active'
expected_result =  pd.DataFrame({'name': ['Alice', 'Charlie'], 'status': ['active', 'active']})
result = test(df0, col0, str0)
assert result.equals(expected_result), 'Test failed'