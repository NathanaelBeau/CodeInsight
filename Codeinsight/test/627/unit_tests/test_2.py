var0 = pd.DataFrame({'word': ['apple', 'banana', 'cherry', 'date']})
str0 = 'word'
int0 = 4
expected_result =  pd.DataFrame({'word': ['apple', 'banana', 'cherry']}).reset_index(drop=True)
result = test(var0, str0, int0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'