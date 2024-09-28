var0 = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'Diana']})
str0 = 'name'
int0 = 3
expected_result =  pd.DataFrame({'name': ['Alice', 'Charlie', 'Diana']}).reset_index(drop=True)
result = test(var0, str0, int0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'