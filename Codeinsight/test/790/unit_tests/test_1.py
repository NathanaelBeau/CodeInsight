var0 = pd.DataFrame({'Name ': ['Alice', 'Bob'], ' Age': [25, 30]})
expected_result =  pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'