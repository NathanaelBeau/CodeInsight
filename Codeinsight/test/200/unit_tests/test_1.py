var0 = pd.DataFrame({'city': ['New York', 'Paris', 'London', 'Tokyo']})
str0 = 'city'
int0 = 5
expected_result =  pd.DataFrame({'city': ['New York', 'London']}).reset_index(drop=True)
result = test(var0, str0, int0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'