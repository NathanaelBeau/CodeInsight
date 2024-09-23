var0 = pd.DataFrame({'A': ['apple', 'banana', 'banana', 'cherry', 'cherry', 'date']})
expected_result =  pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'date']})
result = test(var0)
assert result.equals(expected_result), 'Test failed'