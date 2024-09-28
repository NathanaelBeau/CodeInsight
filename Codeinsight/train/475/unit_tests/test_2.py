df0 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
expected_result =  pd.DataFrame({'Name': ['Alice', 'Charlie'], 'Age': [25, 35]}, index=[0, 2])
result = test(df0)
assert result.equals(expected_result), 'Test failed'